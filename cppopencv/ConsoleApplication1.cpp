﻿#include <OpenCVapp.h>
#include <opencv2/core/utils/logger.hpp>

int nRet = MV_OK;
void* handle = NULL;
CSerialPort st;
int MVSinit();
MV_CC_DEVICE_INFO_LIST stDeviceList;
MV_FRAME_OUT stImageInfo = { 0 };
unsigned char* pData;
extern unsigned char buf[128];
unsigned char sendbuf[128];

//crc16 代码 modbus
#define u8 unsigned char
#define u16 unsigned short
u16 CRC16_MODBUS(u8* msg, int msg_len);
void modbusCMD3reply(unsigned char* c3buf);

// 主机
//例：【01】【03】【00】【00】【00】【04】【CRC高】【CRC低】 一共8个字节
//1）设备地址即为0x01。
//2）功能码0x03。
//3）0x00 0x00，要读取寄存器的高八位地址和低八位地址。
//4）0x00 0x04，读取寄存器的数量，此处为读取4个寄存器。(一个寄存器，两个字节)
//5）CRC L，CRC H。
// 

//从机响应格式：

//设备号	功能码	返回字节个数	数据1	....数据N	CRC H CRC L

//例：【01】【03】【04】【00】【01】【00】【02】【00】【03】【00】【04】【CRC高】【CRC低】

//1）设备地址即为0x01。

//2）功能码0x03，功能为读取保持寄存器值。

//3）0x04，要返回的数据数量，此处为8/2=4。

//4）【00】【01】【00】【02】【00】【03】【00】【04】，返回的数据。

//5）CRC H，CRC L。

#define CMD0 0    //空闲命令；
#define CMD1 1    //
#define CMD2 2     
#define CMD3 3    // 0x03号命令，读可读写模拟量寄存器（保持寄存器）：
#define CMD6 6    // 0x06号命令，读可读写模拟量寄存器（保持寄存器）：
#define CMD10 10     //换背景 

#define SlaveID 1

unsigned int ModbusReceiveCmd = 0;
unsigned int bingX, bingY, angle, radius;
unsigned int readCOMThreadstop = 0;
cv::Mat srcImage100(1024, 1280, CV_8UC1, Scalar(100));
cv::Mat Background(1024, 1280, CV_8UC1, Scalar(100));
cv::Mat srcImageBackground(1024, 1280, CV_8UC1, Scalar(100));
// 
// 线程函数，接收数据
void readCOMThread(void)
{
	while (1)
	{
		unsigned char* ret = NULL;
		ret = st.receive();
		if (ret != NULL)
		{
			printf("receive:");
			for (int i = 0; i < 8; i++)
			{
				printf("%x ", ret[i]);
			}
			printf("\r\n");
			if (ret[0] == SlaveID)
			{
				u16 CRCValue;
				u8 CRCValue_low;
				u8 CRCValue_high;
				CRCValue = CRC16_MODBUS(ret, 6);
				CRCValue_low = CRCValue % 256;
				CRCValue_high = CRCValue / 256;
				if ((ret[6] == CRCValue_low) && (ret[7] == CRCValue_high))
				{
					//printf("CRCValue right %x %x\r\n", CRCValue_low, CRCValue_high);
					//printf(" CMD= %x\r\n", ret[1]);
					if (ret[1] == CMD3)
					{
						ModbusReceiveCmd = CMD3;
					}
					else  if (ret[1] == CMD6)
					{
						ModbusReceiveCmd = CMD6;
					}
					else
					{
						for (int i = 0; i < 5; i++)
						{
							buf[i] = 0;
						}
						printf(" invalid ModbusReceiveCmd %x\r\n", ModbusReceiveCmd);
					}
				}
				else
				{
					for (int i = 0; i < 5; i++)
					{
						buf[i] = 0;
					}
					printf("CRCValue wrong %x %x\r\n", CRCValue_low, CRCValue_high);
				}
			}
			else
			{
				for (int i = 0; i < 5; i++)
				{
					buf[i] = 0;
				}
				printf("Wrong SlaveID \r\n");
			}//
		}

		std::this_thread::sleep_for(std::chrono::milliseconds(10));
		if (readCOMThreadstop == 20)
		{
			readCOMThreadstop = 30;
			std::cout << "readCOMThreadstop\r\n" << std::endl;
			st.close();
			break;
		}
	}
}

cv::Mat srcImage;

void subtractImage(cv::Mat& inputImage1, cv::Mat& inputImage2, cv::Mat& outputImage)
{
	for (int i = 0; i < inputImage1.rows; ++i)
	{
		for (int j = 0; j < inputImage1.cols; ++j)
		{
			int val = inputImage1.at<uchar>(i, j) - inputImage2.at<uchar>(i, j);

			if (val < 0)
				outputImage.at<uchar>(i, j) = 0;

			outputImage.at<uchar>(i, j) = val;
		}
	}
}

int main(int argc, const char* argv[])
{

	bool OPEN_OK;
	float ExposureTime=7000;
	int brightness=0;
	int brightnessCount = 0;
	int BackgroundValue = 0;
	int CMD3delay = 0;
	int coordinate=1;   //检测用，一般要关闭

	cv::Mat  grayImage, fgmaskMOG2, firstImage, curImage, diffImage, diffImage2;//

	Ptr<BackgroundSubtractorMOG2> bgm2 = createBackgroundSubtractorMOG2();
	bgm2->setHistory(20);
	bgm2->setVarThreshold(25);
	bgm2->setDetectShadows(false);

	//cv::utils::logging::setLogLevel(utils::logging::LOG_LEVEL_SILENT);//不再输出日志

	//或
	utils::logging::setLogLevel(utils::logging::LOG_LEVEL_ERROR);//只输出错误日志

	int i = 0;
	char str[5][20];
	ifstream readFile("Setfile.txt");
	if (!readFile)
	{
		printf("Setfile.txt Wrong\r\n");
		char* comx;
		char comN[12] = "\\\\.\\COM10";
		 comx = comN;
		OPEN_OK = st.open(comx, 9600, NOPARITY, 8, TWOSTOPBITS, 1);// ONESTOPBIT=0   无校验位"\\\\.\\COM3"
		if (OPEN_OK)
		{
			printf("com10 OK\r\n");
		}
		else
		{
			printf("com10 err\r\n");
		}

	}
	else
	{
		printf("Setfile.txt OK \r\n");
		while (!readFile.eof())
		{

			readFile >> str[i];
			cout << "str" << i <<"  " << str[i] << endl;
			i++;
		}
		readFile.close();
		//   串口打开

		int Baudrate = stoi(str[1]);
		char* comY;
		comY = str[0];
		printf("comY = %s \r\n", comY);
		printf("Baudrate=%d \r\n", Baudrate);

		OPEN_OK = st.open(comY, 9600, NOPARITY, 8, TWOSTOPBITS, 1);// ONESTOPBIT=0   无校验位"\\\\.\\COM3"
		if (OPEN_OK)
		{
			printf("com OK\r\n");
		}
		else
		{
			printf("com err\r\n");
		}
	}

	
	//工业相机初始化，开始取流
	MVSinit();

	MVCC_INTVALUE stIntVal;
	memset(&stIntVal, 0, sizeof(MVCC_INTVALUE));
	nRet = MV_CC_GetIntValue(handle, "Width", &stIntVal);
	if (MV_OK != nRet)
	{
		printf("Get Width fail! nRet [0x%x]\n", nRet);
		return nRet;
	}
	printf("Current Width [%d]\n", stIntVal.nCurValue);
	uint  ImageWidth = stIntVal.nCurValue;
	nRet = MV_CC_GetIntValue(handle, "Height", &stIntVal);
	if (MV_OK != nRet)
	{
		printf("Get Height fail! nRet [0x%x]\n", nRet);
		return nRet;
	}
	printf("Current Height [%d]\n", stIntVal.nCurValue);
	uint  ImageHeight = stIntVal.nCurValue;
	//接收串口线程打开
	thread thread1(readCOMThread);

//	cv::Mat Background(ImageHeight, ImageWidth, CV_8UC1, Scalar(100));
//	cv::Mat srcImageBackground(ImageHeight, ImageWidth, CV_8UC1, Scalar(100));
	cv::Mat srcImage;
	

	
	while (true)
	{
		//clock_t startTime, endTime;
		//startTime = clock();

GETB:		nRet = MV_CC_GetImageBuffer(handle, &stImageInfo, 1000);
		if (nRet == MV_OK)
		{   //  Width[%d], Height[%d], nFrameNum[%d]
			// printf("Get Frame: W[%d], H[%d], n[%d]\n",
			//	stImageInfo.stFrameInfo.nWidth, stImageInfo.stFrameInfo.nHeight, stImageInfo.stFrameInfo.nFrameNum);
		}
		else
		{
			printf("No data[0x%x]\n", nRet);
			
			// Set trigger mode as off
			nRet = MV_CC_SetEnumValue(handle, "TriggerMode", 0);   // off
			if (MV_OK != nRet)
			{
				printf("Set Trigger Mode fail! nRet [0x%x]\n", nRet);
				//break;
			}
			else
			{
				printf("Set Trigger Mode OK nRet [0x%x]\n", nRet);
			}
			waitKey(100);
			goto  GETB;
			//break;
		}

		srcImage = cv::Mat(stImageInfo.stFrameInfo.nHeight, stImageInfo.stFrameInfo.nWidth, CV_8UC1, stImageInfo.pBufAddr);
		bgm2->apply(srcImage, diffImage);
		srcImage.copyTo(srcImageBackground);

		cv::Scalar meanview = cv::mean(srcImage);
	    float MeanOfSrcImage = meanview.val[0];//.val[0]表示第一个通道的均值
		cv::Scalar diffImagemeanview = cv::mean(diffImage);
		float MeanOfDiffImage = diffImagemeanview.val[0];//.val[0]表示第一个通道的均值	
	//	printf("亮度 %lf, 前景 %lf， 曝光= %lf\r\n", MeanOfSrcImage, MeanOfDiffImage, ExposureTime);	
		//前景正常，再判断取流亮度是否符合要求。
		if (MeanOfDiffImage < 5)   
		{
			//if (MeanOfSrcImage < 64 || MeanOfSrcImage > 76)//
			if (MeanOfSrcImage < 54 || MeanOfSrcImage > 66)
			{
				brightness = 0;
				printf("前景超出范围：亮度 %lf, 前景 %lf， 曝光= %lf\r\n", MeanOfSrcImage, MeanOfDiffImage, ExposureTime);

			}
		}
		else    //前景发生巨大变化
		{
			//printf("前景亮度，突变= %lf\r\n", MeanOfDiffImage);
		}

		//亮度不符合要求，进行自适应调整
		if (brightness == 0)//亮度不符合要求
		{
				if (MeanOfSrcImage > 55 && MeanOfSrcImage < 65)  //80 120      65 75
				{
					brightness = 1;//亮度符合要求
					if (BackgroundValue != 1)//1代表背景获得。
					{
						BackgroundValue = 1;
						srcImage.copyTo(Background);
						stringstream str2;
						str2 << "D:/Program Files/opencv/pictrue/MVC/" << "Background.png";
						cout << str2.str() << endl;
						imwrite(str2.str(), Background);
					}
				}
				else
				{
				//	brightness = 0;
					nRet = MV_CC_FreeImageBuffer(handle, &stImageInfo);
					if (MV_OK != nRet)
					{
						printf("MV_CC_FreeImageBuffer error  [0x%x]\n", nRet);
						//break;
					}
					nRet = MV_CC_StopGrabbing(handle);
					if (MV_OK != nRet)
					{
						printf("Stop Grabbing fail! nRet [0x%x]\n", nRet);
					}
					else
					{
					//	printf("Stop Grabbing OK nRet [0x%x]\n", nRet);
					}
					if (MeanOfSrcImage < 60)//亮度小，快门增加快，基数大比例小   70
					{
						ExposureTime = ExposureTime + (60 - MeanOfSrcImage) * 100;
					}
					else//亮度大，快门较少慢，基数小，比例大。
					{
						ExposureTime = ExposureTime + (60 - MeanOfSrcImage) * 50;
					}
					
					if (ExposureTime < 1000)
					{
						ExposureTime = 1000;
					}
					nRet = MV_CC_SetFloatValue(handle, "ExposureTime", ExposureTime);

					printf("调整曝光= %lf\r\n", ExposureTime);
					//设置曝光时间us
					if (MV_OK != nRet)
					{
						printf("Set GainAuto fail! nRet [0x%x]\n", nRet);
					}
					nRet = MV_CC_StartGrabbing(handle);
					if (MV_OK != nRet)
					{
						printf("Start Grabbing fail! nRet [0x%x]\n", nRet);
					}
					goto Wend;
				}		
		}

		coordinate = 1;
		if ((coordinate == 0) &&(MeanOfDiffImage < 5 ) &&(brightness==1) )
		{
			std::vector<std::vector<cv::Point>> contours101;
			std::vector<cv::Vec4i> hierarchy101;
			Mat srcImage101, srcImage102;
			srcImage.copyTo(srcImage101);
			srcImage.copyTo(srcImage102);
			adaptiveThreshold(srcImage101, srcImage101, 255, ADAPTIVE_THRESH_GAUSSIAN_C, THRESH_BINARY, 25, 0);
		//	imshow("coordinateThreshold", srcImage101);
			Mat k = getStructuringElement(MORPH_RECT, Size(5, 5), Point(-1, -1));
			morphologyEx(srcImage101, srcImage101, MORPH_OPEN, k);
		//	imshow("coordinateMORPH_OPEN", srcImage101);
			k = getStructuringElement(MORPH_RECT, Size(7, 7), Point(-1, -1));
			morphologyEx(srcImage101, srcImage101, MORPH_CLOSE, k);
			imshow("coordinateMORPH_CLOSE", srcImage101);

			Canny(srcImage101, srcImage101, 100, 200, 5, false);
			cv::findContours(srcImage101, contours101, hierarchy101, cv::RETR_EXTERNAL, cv::CHAIN_APPROX_NONE, cv::Point(0, 0));//CHAIN_APPROX_SIMPLE

			int max=0, maxi=0;
			for (int i = 0; i < contours101.size(); i++)
			{
				if (max < contours101[i].size())
				{
					max = contours101[i].size();
					maxi = i;
				//	printf(" %d  %d\r\n", i, contours101[maxi].size());
				}
			}

		//	printf("测量轮廓数量= %d  最大轮廓大小=%d\r\n", contours101.size(), contours101[maxi].size());
			drawContours(srcImage101, contours101, maxi, cv::Scalar(255, 175, 255), 1, 8, hierarchy101);
			cv::imshow("srcImage101canny+drawContours", srcImage101);

			if (max > 500)
			{
				//drawContours(srcImage, contours, i, cv::Scalar(255, 175, 255), 2, 8, hierarchy);
				RotatedRect rect = minAreaRect(contours101[maxi]);
				Point2f P[4];
				rect.points(P);
				vector<int> X_Contours;
				for (int j = 0; j <= 3; j++)
				{
					X_Contours.push_back(P[j].x);
					X_Contours.push_back(P[(j + 1) % 4].x);
					line(srcImage102, P[j], P[(j + 1) % 4], Scalar(255, 255, 255), 1);
				}
				float distanceP0P1; 
				float distanceP1P2;
				float distanceline;
				distanceP0P1 = powf(P[0].y - P[1].y, 2) + powf(P[1].x - P[0].x, 2);
				distanceP1P2 = powf(P[2].y - P[1].y, 2) + powf(P[2].x - P[1].x, 2);
					
			//	circle(srcImage102, P[0], 3, 255, 5, 8, 0);
			//	circle(srcImage102, P[1], 7, 255, 5, 8, 0);
			//	circle(srcImage102, P[2], 11, 255, 5, 8, 0);
			//	circle(srcImage102, P[3], 15, 255, 5, 8, 0);
				float y = 0, x = 0, angle=0;
				if (distanceP0P1 >= distanceP1P2)
				{
					 y =-(P[1].y - P[0].y) ;
					 x = P[1].x - P[0].x;
				//	 printf("distanceP0P1 >= distanceP1P2 y=%f   x=%f \r\n", y, x);
					 angle = atan2(y, x);
					 angle = angle * 57.3;
					 distanceline = sqrt(distanceP0P1);
				//	 printf("y=%f  x=%f angle=%f  P[0].y=%f   P[1].y=%f \r\n", y, x, angle, P[0].y, P[1].y);
				}
				else
				{
					y = -(P[2].y - P[1].y);
					x = P[2].x - P[1].x;
				//	printf("distanceP0P1 < distanceP1P2 y=%f   x=%f \r\n", y, x);
					angle = atan2(y, x);
					angle = angle * 57.3;
					distanceline = sqrt(distanceP1P2);
				//	printf("y=%f  x=%f angle=%f  P[1].y=%f   P[2].y=%f \r\n", y, x, angle, P[1].y, P[2].y);
				}	
				
				Point middle;
				middle.x = (P[0].x + P[2].x)/2;
				middle.y = (P[0].y + P[2].y)/2;
				circle(srcImage102, middle, 6, 255, 1, 8, 0);

				float Pcoefficient= distanceline/220;

				char str[50];
				Point TexP1(100, 200), TexP2(100, 300), TexP2Line(100, 400), TexP2LineA(100, 500);
				sprintf_s(str, "angle_correct=%f", angle);
				putText(srcImage102, str, TexP1, FONT_HERSHEY_SIMPLEX, 1, 255, 3);
				sprintf_s(str, "x_offset=%d y_offset=%d", middle.x, middle.y);
				putText(srcImage102, str, TexP2, FONT_HERSHEY_SIMPLEX, 1, 255, 3);
				sprintf_s(str, "distanceline = %f Pcoefficient= %f", distanceline, Pcoefficient);
				putText(srcImage102, str, TexP2Line, FONT_HERSHEY_SIMPLEX, 1, 255, 3);
				distanceline = distanceline /3.07;
				sprintf_s(str, "line = %f ", distanceline);
				putText(srcImage102, str, TexP2LineA, FONT_HERSHEY_SIMPLEX, 1, 255, 3);
			}
			cv::resize(srcImage102, srcImage102, Size(800, 640), 0.5, 0.5, INTER_LINEAR);
			cv::imshow("srcImage102", srcImage102);
			coordinate = 0;
			waitKey(300);
		}

		//CMD6命令，暂时不用。
		if (ModbusReceiveCmd == CMD6&& BackgroundValue == 1)  //开始抓拍并计算好像可以不用。
		{
			//printf("buf[1] == 0x06");
			stringstream str;
			str << "D:/Program Files/opencv/pictrue/MVC/" << 1 << ".png";
			cout << str.str() << endl;
			imwrite(str.str(), srcImage);
			st.send(buf, 8);
			for (int i = 0; i < 5; i++)
			{
				buf[i] = 0;
			}
			ModbusReceiveCmd = CMD0;
		}

		if ((ModbusReceiveCmd == CMD3) && (BackgroundValue == 1) &&(MeanOfDiffImage<5) &&(brightness == 1) )  //返回坐标参数
		{
			//接收到CD3命令，已经有背景，MeanOfDiffImage（前景没变化）,亮度稳定
			printf("亮度 %lf, 前景 %lf， 曝光= %lf\r\n", MeanOfSrcImage, diffImagemeanview, ExposureTime);
			cv::Mat srcImage1(srcImage.rows, srcImage.cols, CV_8UC1, Scalar(100));
			uchar val=0;
			for (int i = 0; i < srcImage.rows; ++i)
			{
					for (int j = 0; j < srcImage.cols; ++j)
					{
						if (srcImage.at<uchar>(i, j) > Background.at<uchar>(i, j))
						{
							val = srcImage.at<uchar>(i, j) - Background.at<uchar>(i, j);
							if (val < 20) { val = 0; } //原先10  20  50
						}
						else
						{
							val = Background.at<uchar>(i, j)- srcImage.at<uchar>(i, j);
							if (val < 255) { val = 0; }//原先 50
						}
						srcImage1.at<uchar>(i, j) = val;
					}
			}

			unsigned char* cmdbufm = OpenCVcaculate(srcImage1, srcImage, 8);   //srcImage为原图，srcImage1为减法后的图

			modbusCMD3reply(cmdbufm);
			for (int i = 0; i < 5; i++)
			{
				buf[i] = 0;
			}
			ModbusReceiveCmd = CMD10;
			CMD3delay = 0;
			printf("CMD3 finish  \r\n");
		}
		//在空闲的时候，延时2s换背景。
		if (BackgroundValue == 1 && ModbusReceiveCmd == CMD10 && (MeanOfDiffImage < 5))
		{
			CMD3delay++;
			if (CMD3delay > 3)   //10帧等待。10帧等待，大概300ms
			{
				std::vector<std::vector<cv::Point>> contours;
				std::vector<cv::Vec4i> hierarchy;
				int maxcontours=0;
				int maxcontoursIndex = 0;
				srcImage.copyTo(srcImage100);
				adaptiveThreshold(srcImage100, srcImage100, 255, ADAPTIVE_THRESH_GAUSSIAN_C, THRESH_BINARY, 25, 0);
				imshow("srcImage100adaptiveThreshold", srcImage100);
				Mat k = getStructuringElement(MORPH_RECT, Size(5, 5), Point(-1, -1));
				morphologyEx(srcImage100, srcImage100, MORPH_OPEN, k);
				imshow("srcImage100MORPH_OPEN", srcImage100);
				k = getStructuringElement(MORPH_RECT, Size(9, 9), Point(-1, -1));   
				morphologyEx(srcImage100, srcImage100, MORPH_CLOSE, k);
				imshow("srcImage100MORPH_CLOSE", srcImage100);

				Point test(500, 600);
				circle(srcImage100, test, 30, 255, 7, 8, 0);
				Canny(srcImage100, srcImage100, 100, 200, 5, false);
				cv::findContours(srcImage100, contours, hierarchy, cv::RETR_EXTERNAL, cv::CHAIN_APPROX_SIMPLE, cv::Point(0, 0));
				printf("背景轮廓数量 %d\r\n",contours.size());

				for (int i = 0; i < contours.size(); ++i)
				{
					if (maxcontours < contours[i].size())
					{
						maxcontours = contours[i].size();
						maxcontoursIndex = i;
					}
				}
				printf("背景轮廓数量=%d maxcontoursIndex=%d maxcontours= %d \r\n", contours.size(), maxcontoursIndex, maxcontours);
				drawContours(srcImage100, contours, maxcontoursIndex, cv::Scalar(255, 175, 255), 5, 8, hierarchy);		
				cv::resize(srcImage100, srcImage100, Size(800, 640), 0.5, 0.5, INTER_LINEAR);
			//	imshow("srcImage100", srcImage100);
				cv::imshow("srcImage100canny+drawContours", srcImage100);
				if (maxcontours < 500)
				{
					srcImageBackground.copyTo(Background);
					stringstream str1;
					str1 << "D:/Program Files/opencv/pictrue/MVC/" << "Background3.png";
					imwrite(str1.str(), Background);

					CMD3delay = 0;
					printf("背景换，饼已经移走\r\n");
				}
				else 
				{
					printf("背景不换，饼没有移走\r\n");
				}
				ModbusReceiveCmd = CMD0;
				CMD3delay = 0; //作用，不再进入ModbusReceiveCmd == CMD10，的循环，本次换背景结束
			}
		}
	
		nRet = MV_CC_FreeImageBuffer(handle, &stImageInfo);
		if (MV_OK != nRet)
		{
			printf("MV_CC_FreeImageBuffer error  [0x%x]\n", nRet);
			//break;
		}
		Wend:
		if (waitKey(50) == 32)
		{
			readCOMThreadstop = 20;
			std::cout << "waitKey stop:\r\n" << std::endl;
			break;
		} 
	}

	// Stop grab image
	nRet = MV_CC_StopGrabbing(handle);
	if (MV_OK != nRet)
	{
		printf("Stop Grabbing fail! nRet [0x%x]\n", nRet);
		//break;
	}
	else
	{
		printf("Stop Grabbing OK nRet [0x%x]\n", nRet);
	}
	// Close device

	readCOMThreadstop = 20;//关闭串口
	while (readCOMThreadstop == 20)
	{
		int i;
		for (i = 0; i < 100; i++)
		{
			std::this_thread::sleep_for(std::chrono::milliseconds(10));
			if (readCOMThreadstop == 30)
			{
				printf("readCOMThreadstop = %d\n", i);
				break;
			}
		}	
	}

	nRet = MV_CC_CloseDevice(handle);
	if (MV_OK != nRet)
	{
		printf("ClosDevice fail! nRet [0x%x]\n", nRet);
		//break;
	}
	else
	{
		printf("ClosDevice OK! nRet [0x%x]\n", nRet);
	}

	// Destroy handle
	nRet = MV_CC_DestroyHandle(handle);
	if (MV_OK != nRet)
	{
		printf("Destroy Handle fail! nRet [0x%x]\n", nRet);
		//break;
	}
	else
	{
		printf("Destroy Handle OK! nRet [0x%x]\n", nRet);
	}
//	OpenCVcaculate(srcImage, srcImage, 255);
	destroyAllWindows();
	std::exit( 0 );

}

int MVSinit()
{	// Enum device

	memset(&stDeviceList, 0, sizeof(MV_CC_DEVICE_INFO_LIST));  //
	nRet = MV_CC_EnumDevices(MV_GIGE_DEVICE, &stDeviceList);

	printf("Enum Devices nRet [0x%x]\n", nRet);
	if (MV_OK != nRet)
	{
		printf("Enum Devices fail! nRet [0x%x]\n", nRet);
		return -1;
	}

	if (stDeviceList.nDeviceNum > 0)
	{
		for (unsigned int i = 0; i < stDeviceList.nDeviceNum; i++)
		{
			printf("Find [device %d]:\n", i);
			MV_CC_DEVICE_INFO* pDeviceInfo = stDeviceList.pDeviceInfo[i];
			if (NULL == pDeviceInfo)
			{
				break;
			}
			//PrintDeviceInfo(pDeviceInfo);
		}
	}
	else
	{
		printf("Find No Devices!\n");
		return -1;
	}

	// input the format to convert
	unsigned int nFormat = 0;

	// select device to connect
	printf("Please Input camera index(0-%d):", stDeviceList.nDeviceNum - 1);
	unsigned int nIndex = 0;
	//scanf("%d", &nIndex);
	if (nIndex >= stDeviceList.nDeviceNum)
	{
		printf("Input error!\n");
		return -1;
	}

	// Select device and create handle
	nRet = MV_CC_CreateHandle(&handle, stDeviceList.pDeviceInfo[nIndex]);
	if (MV_OK != nRet)
	{
		printf("Create Handle fail! nRet [0x%x]\n", nRet);
		return -1;
	}
	else
	{
		printf("Create Handle OK! nRet [0x%x]\n", nRet);
	}

	// open device
	nRet = MV_CC_OpenDevice(handle, MV_ACCESS_Exclusive, 0);
	if (MV_OK != nRet)
	{
		printf("Open Device fail! nRet [0x%x]\n", nRet);
		return -1;
	}
	else
	{
		printf("Open Device OK! nRet [0x%x]\n", nRet);
	}

	// Detection network optimal package size(It only works for the GigE camera)
	if (stDeviceList.pDeviceInfo[nIndex]->nTLayerType == MV_GIGE_DEVICE)
	{
		int nPacketSize = MV_CC_GetOptimalPacketSize(handle);
		if (nPacketSize > 0)
		{
			nRet = MV_CC_SetIntValue(handle, "GevSCPSPacketSize", nPacketSize);
			if (nRet != MV_OK)
			{
				printf("Warning: Set Packet Size fail nRet [0x%x]!", nRet);
				return -1;
			}
			else
			{
				printf("nPacketSize [0x%d]!", nPacketSize);
			}
		}
		else
		{
			printf("Warning: Get Packet Size fail nRet [0x%d]!", nPacketSize);
		}
	}

	// Set trigger mode as off
	nRet = MV_CC_SetEnumValue(handle, "TriggerMode", 0);   // off
	if (MV_OK != nRet)
	{
		printf("Set Trigger Mode fail! nRet [0x%x]\n", nRet);
		//break;
	}
	else
	{
		printf("Set Trigger Mode OK nRet [0x%x]\n", nRet);
	}

	// Get payload size
	MVCC_INTVALUE stParam;
	memset(&stParam, 0, sizeof(MVCC_INTVALUE));
	nRet = MV_CC_GetIntValue(handle, "PayloadSize", &stParam);
	if (MV_OK != nRet)
	{
		printf("Get PayloadSize fail! nRet [0x%x]\n", nRet);
		//break;
	}
	else
	{
		printf("Get PayloadSize OK nRet [0x%d]\n", stParam.nCurValue);
	}
	unsigned int  g_nPayloadSize = stParam.nCurValue;

	// 设置网络最佳的包大小，设置相机的触发模式
	// Detection network optimal package size(It only works for the GigE camera)
	if (stDeviceList.pDeviceInfo[nIndex]->nTLayerType == MV_GIGE_DEVICE)
	{
		int nPacketSize = MV_CC_GetOptimalPacketSize(handle);
		if (nPacketSize > 0)
		{
			nRet = MV_CC_SetIntValue(handle, "GevSCPSPacketSize", nPacketSize);
			if (nRet != MV_OK)
			{
				printf("Warning: Set Packet Size fail nRet [0x%x]!", nRet);
			}
			else
			{
				printf("Warning: Set Packet Size OK nRet [0x%d]!", nPacketSize);
			}
		}
		else
		{
			printf("Warning: Get Packet Size fail nRet [0x%x]!", nPacketSize);
		}
	}

	nRet = MV_CC_SetExposureAutoMode(handle, 0);//Continuous:2,off:0;once:1;
	if (MV_OK != nRet)
	{
		printf("Set ExposureAutoMode fail! nRet [0x%x]\n", nRet);
		return nRet;
	}

	nRet = MV_CC_SetFloatValue(handle, "AcquisitionFrameRate", 30);
	if (MV_OK != nRet)
	{
		printf("Set AcquisitionFrameRate fail! nRet [0x%x]\n", nRet);
		return nRet;
	}

	nRet = MV_CC_SetBoolValue(handle, "DigitalShiftEnable", 1);//
	if (MV_OK != nRet)
	{
		printf("Set DigitalShiftEnable fail! nRet [0x%x]\n", nRet);
		return nRet;
	}

	nRet = MV_CC_SetEnumValue(handle, "GainAuto",0 );   //Continuous:2,off:0;once:1;
	if (MV_OK != nRet)
	{
		printf("Set GainAuto fail! nRet [0x%x]\n", nRet);
		//break;
	}

	nRet = MV_CC_SetFloatValue(handle, "ExposureTime", 5000);   //设置曝光时间us
	if (MV_OK != nRet)
	{
		printf("Set GainAuto fail! nRet [0x%x]\n", nRet);
		//break;
	}

	nRet = MV_CC_SetFloatValue(handle, "Gain", 11);
	if (MV_OK != nRet)
	{
		printf("Set Gain fail! nRet [0x%x]\n", nRet);
		return nRet;
	}
	// Start grab image
	nRet = MV_CC_StartGrabbing(handle);
	if (MV_OK != nRet)
	{
		printf("Start Grabbing fail! nRet [0x%x]\n", nRet);
		//break;
	}
	else
	{
		printf("Start Grabbing OK! nRet [0x%x]\n", nRet);
	}

	memset(&stImageInfo, 0, sizeof(MV_FRAME_OUT));
	/*pData = (unsigned char*)malloc(sizeof(unsigned char) * (g_nPayloadSize));
	if (pData == NULL)
	{
		printf("Allocate memory failed.\n");
		//break;
	}
	else
	{
		printf("Allocate memory OK.\n");
	}*/
	

}

u16 CRC16_MODBUS(u8* msg, int msg_len)
{
	//CRC校验
	u16 i, j, tmp, CRC16;
	CRC16 = 0xFFFF; //CRC寄存器初始值
	for (i = 0; i < msg_len; i++)
	{
		CRC16 ^= msg[i];
		for (j = 0; j < 8; j++)
		{
			tmp = (u16)(CRC16 & 0x0001);
			CRC16 >>= 1;
			if (tmp == 1)
			{
				CRC16 ^= 0xA001; //异或多项式
			}
		}
	}
	return CRC16;
}

void modbusCMD3reply(unsigned char* c3buf)
{
	//返回数据长度(12=head3+内容8+CRC2)：圆心 x 2字节 x 2字节；角度 2字字节；直径 2字节
	sendbuf[0] = SlaveID;
	sendbuf[1] = 0x03;    // 功能码
	sendbuf[2] = 0x4;     // 八个字节
	sendbuf[3] = c3buf[1];
	sendbuf[4] = c3buf[0];
	sendbuf[5] = c3buf[3];
	sendbuf[6] = c3buf[2];
	sendbuf[7] = c3buf[5];  //角度返回值为真实值的10倍，相当于精确到0.1 比如15.1°  最大值为30度。
	sendbuf[8] = c3buf[4];
	sendbuf[9] = c3buf[7];
	sendbuf[10] = c3buf[6];
	unsigned int CRCValue = CRC16_MODBUS(sendbuf, 11);
	sendbuf[11] = CRCValue % 256;   //crclow
	sendbuf[12] = CRCValue / 256;   //crchigh
	printf("CRCValue sendbuf ");
	st.send(sendbuf, 13);
	for (int i = 0; i <= 12; i++)
	{
		printf("%x  ", sendbuf[i]);
	}
	printf("\r\n");
}
