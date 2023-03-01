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
		cout << "��ȷ��ͼ���ļ������Ƿ���ȷ" << endl;
		return -1;
	}
	imshow("img", gray);
	//cvtColor(img, gray, COLOR_BGR2GRAY);
	GaussianBlur(gray, gray, Size(9, 9), 10, 10);  //ƽ���˲�
												 //���Բ��
	vector<Vec3f> circles;
	double dp = 2; //
	double minDist = 10;  //����Բ��֮�����С����
	double	param1 = 40;  //Canny��Ե������ֵ
	double	param2 = 50;  //�ۼ�����ֵ
	int min_radius = 15;  //Բ�ΰ뾶����Сֵ
	int max_radius = 25;  //Բ�ΰ뾶�����ֵ
	HoughCircles(gray, circles, HOUGH_GRADIENT, dp, minDist, param1, param2,min_radius, max_radius);
	//ͼ���б�ǳ�Բ��
    int sum=0;
    float radius; 
    for (size_t i = 0; i < circles.size(); i++)
	{
		radius = circles[i][2];
        sum+=radius;
	}
    int circle_number=circles.size();
    float radius_avg;
    if (circle_number!=0) radius_avg=sum/circle_number;
    else radius=0;
	for (size_t i = 0; i < circles.size(); i++)
	{
		//��ȡԲ��
		Point center(cvRound(circles[i][0]), cvRound(circles[i][1]));
		circle(gray, center, cvRound(radius_avg), Scalar(0, 0, 255), -1, 8, 0);
	}
	imshow("circle", gray);

	waitKey(0);
	return 0;
}

/*
    //����Բ���һ������,��ͼ���������㣬Ȼ�����������ʶ��
    Mat element=getStructuringElement(MORPH_RECT,Size(9,9));
    Mat kimg;
    morphologyEx(gray,kimg,MORPH_OPEN,element);
    //morphologyEx(img,kimg,MORPH_ERODE,element);
	imshow("kimg", kimg);
    //����������
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
