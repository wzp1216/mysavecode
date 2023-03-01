#include <opencv2/opencv.hpp>
#include <iostream>
#include <cmath>
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
		cout << "请确认图像文件名称是否正确" << endl;
		return -1;
	}
	imshow("img", img);
	Mat gray;
	cvtColor(img, gray, COLOR_BGR2GRAY);
	GaussianBlur(gray, gray, Size(9, 9), 10, 10);  //平滑滤波
                                                 //
	imshow("gray", gray);
												 //检测圆形
	vector<Vec3f> circles;
	double dp = 2; //
	double minDist = 10;  //两个圆心之间的最小距离
	double	param1 = 40;  //Canny边缘检测的较大阈值
	double	param2 = 50;  //累加器阈值
	int min_radius = 15;  //圆形半径的最小值
	int max_radius = 25;  //圆形半径的最大值
	HoughCircles(gray, circles, HOUGH_GRADIENT, dp, minDist, param1, param2,
		min_radius, max_radius);

	//图像中标记出圆形
    int sum=0;
	for (size_t i = 0; i < circles.size(); i++)
	{
		//读取圆心
		Point center(cvRound(circles[i][0]), cvRound(circles[i][1]));
		//读取半径
		int radius = cvRound(circles[i][2]);
        sum+=radius;
		//绘制圆心
		circle(img, center, 3, Scalar(0, 255, 0), -1, 8, 0);
		//绘制圆
		circle(img, center, radius, Scalar(0, 0, 255), 2, 8, 0);
	}
	imshow("end", img);
    //所有圆组成一个区域

	waitKey(0);
	return 0;
}
