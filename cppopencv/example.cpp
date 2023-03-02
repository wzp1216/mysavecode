#include <opencv2/opencv.hpp>
#include <iostream>
#include <cmath>
#include <string>
#include <vector>

using namespace cv;
using namespace std;

void drawapp(Mat result,Mat img2){
    for(int i=0;i<result.rows;i++){
        if(i==result.rows-1){
            Vec2i point1=result.at<Vec2i>(i);
            Vec2i point2=result.at<Vec2i>(0);
            line(img2,point1,point2,Scalar(0,0,255),2,8,0);
            break;
        }
        Vec2i point1=result.at<Vec2i>(i);
        Vec2i point2=result.at<Vec2i>(i+1);
        line(img2,point1,point2,Scalar(0,0,255),2,8,0);
    }
}
int main(int argc,char* argv[])
{
    string filename=argv[1];
	Mat gray= imread(filename,IMREAD_GRAYSCALE);

    if (gray.empty())
	{
		cout << "请确认图像文件名称是否正确" << endl;
		return -1;
	}
	imshow("img", gray);
	//cvtColor(img, gray, COLOR_BGR2GRAY);
	GaussianBlur(gray, gray, Size(9, 9), 10, 10);  //平滑滤波
												 //检测圆形
	vector<Vec3f> circles;
	double dp = 2; //
	double minDist = 10;  //两个圆心之间的最小距离
	double	param1 = 40;  //Canny边缘检测的阈值
	double	param2 = 50;  //累加器阈值
	int min_radius = 15;  //圆形半径的最小值
	int max_radius = 25;  //圆形半径的最大值
	HoughCircles(gray, circles, HOUGH_GRADIENT, dp, minDist, param1, param2,min_radius, max_radius);
	//图像中标记出圆形
    int sum=0;
    float radius; 
    for (size_t i = 0; i < circles.size(); i++)	{
		radius = circles[i][2];
        sum+=radius;
	}
    int circle_number=circles.size();
    float radius_avg;
    vector<Point> cpoints;
    if (circle_number!=0) radius_avg=sum/circle_number;
    else radius=0;
	//for (size_t i = 0; i < circles.size(); i++)
	for (auto p=circles.begin();p!=circles.end();p++){
		//读取圆心
		Point center(cvRound((*p)[0]), cvRound((*p)[1]));
        cpoints.push_back(center);
		circle(gray, center, cvRound(radius_avg), Scalar(0, 0, 255), -1, 8, 0);
	}
    Mat bin_gray;
    threshold(gray,bin_gray,10,255,THRESH_BINARY);
	imshow("bin", bin_gray);
    Point2f key_center;
    float big_radius=0;
    minEnclosingCircle(cpoints,key_center,big_radius);
    circle(bin_gray,key_center,cvRound(big_radius),Scalar(0,0,255),2,LINE_AA);
    imshow("end",bin_gray);

	waitKey(0);
	return 0;
}

/*
    //所有圆组成一个区域,对图像做开运算，然后进行六边形识别；
    Mat element=getStructuringElement(MORPH_RECT,Size(9,9));
    Mat kimg;
    morphologyEx(gray,kimg,MORPH_OPEN,element);
    //morphologyEx(img,kimg,MORPH_ERODE,element);
	imshow("kimg", kimg);
    //发现六边形
    vector<vector<Point>> contours;
    vector<Vec4i> hierarchy;
    findContours(kimg,contours,hierarchy,0,2,Point());
    for (size_t t=0;t<contours.size();t++){
        Mat polyimg;
        approxPolyDP(contours[t],polyimg,4,true);
        drawapp(polyimg,kimg);
    }
	imshow("polt", kimg);
*/
