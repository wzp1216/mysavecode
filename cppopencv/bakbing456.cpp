#include <opencv2/opencv.hpp>
#include <iostream>
#include <string>
#include <vector>

using namespace cv;
using namespace std;

int main(int argc,char* argv[])
{
    string filename=argv[1];
	Mat img = imread(filename);
	if (img.empty())
	{
		cout << "��ȷ��ͼ���ļ������Ƿ���ȷ" << endl;
		return -1;
	}
	imshow("img", img);
	Mat gray;
	cvtColor(img, gray, COLOR_BGR2GRAY);
	GaussianBlur(gray, gray, Size(7, 7), 10, 10);  //ƽ���˲�
                                                 //
	imshow("gray", gray);
												 //���Բ��
	vector<Vec3f> circles;
	double dp = 2; //
	double minDist = 8;  //����Բ��֮�����С����
	double	param1 = 20;  //Canny��Ե���Ľϴ���ֵ
	double	param2 = 40;  //�ۼ�����ֵ
	int min_radius = 5;  //Բ�ΰ뾶����Сֵ
	int max_radius = 15;  //Բ�ΰ뾶�����ֵ
	HoughCircles(gray, circles, HOUGH_GRADIENT, dp, minDist, param1, param2,
		min_radius, max_radius);

	//ͼ���б�ǳ�Բ��
	for (size_t i = 0; i < circles.size(); i++)
	{
		//��ȡԲ��
		Point center(cvRound(circles[i][0]), cvRound(circles[i][1]));
		//��ȡ�뾶
		int radius = cvRound(circles[i][2]);
		//����Բ��
		circle(img, center, 3, Scalar(0, 255, 0), -1, 8, 0);
		//����Բ
		circle(img, center, radius, Scalar(0, 0, 255), 3, 8, 0);
	}

	//��ʾ���
	imshow("end", img);
	waitKey(0);
	return 0;
}
