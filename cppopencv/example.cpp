#include <opencv2/opencv.hpp>
#include <iostream>
#include <cmath>
#include <string>
#include <vector>

using namespace cv;
using namespace std;

float getDistance(Point a,Point b){
    float dis;
    dis=sqrtf(powf((a.x-b.x),2)+powf((a.y-b.y),2));
    return dis;
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
	GaussianBlur(gray, gray, Size(3, 3), 10, 10);  //平滑滤波
	vector<Vec3f> circles;
	double dp = 2; //
	double minDist = 20;  //两个圆心之间的最小距离
	double	param1 = 50;  //Canny边缘检测的阈值
	double	param2 = 60;  //累加器阈值
	int min_radius = 10;  //圆形半径的最小值
	int max_radius = 30;  //圆形半径的最大值
	HoughCircles(gray, circles, HOUGH_GRADIENT, dp, minDist, param1, param2,min_radius, max_radius);
	//111图像中找出圆形
    int sum=0;
    int circle_number=circles.size();  
    if (circle_number!=0) 
        cout<<"find circles:"<<circle_number<<endl;
    else return 0;
    float radius_avg=0;
    vector<Point> cpoints;  //圆心
	//222图像画圆
    for (size_t i = 0; i < circles.size(); i++)	{
		Point center(cvRound(circles[i][0]), cvRound(circles[i][1]));
        cpoints.push_back(center);
	    float 	radius = circles[i][2];
        sum+=radius;
		circle(gray, center, cvRound(radius), Scalar(0, 0, 255), -1, 8, 0);
	}
    if (circle_number!=0) radius_avg=sum/circle_number;  //计算平均半径
	imshow("img", gray);
	//333 找出内接圆
    Mat bin_gray;
    threshold(gray,bin_gray,10,255,THRESH_BINARY);
    Point2f key_center;   //中心
    float big_radius=0;    
    minEnclosingCircle(cpoints,key_center,big_radius);  //最小内接圆，求中心;
    circle(bin_gray,key_center,cvRound(big_radius),Scalar(0,0,255),2,LINE_AA);
	for (auto p=cpoints.begin();p!=cpoints.end();p++){
        if(getDistance((*p),key_center)>15*radius_avg)
            cpoints.erase(p);
        else
            circle(bin_gray,*p,cvRound(radius_avg),Scalar(0,0,255),2,LINE_AA);
	}
	imshow("cir_add", bin_gray);
	//444 找出六边形
    vector<float> dist;  
    vector<Point> liu;  
	for (auto p=cpoints.begin();p!=cpoints.end();p++){
        dist.push_back(getDistance((*p),key_center));
    }
    sort(dist.begin(),dist.end());
    float min_dist=*(dist.end()-7);
	for (auto p=cpoints.begin();p!=cpoints.end();p++){
        if ((getDistance((*p),key_center)-min_dist)>0.001)
            liu.push_back(*p);
    }
    cout<<"fonund key point:"<<liu.size()<<endl;
    sort(liu.begin(),liu.end());
    /*
	for (auto p=liu.begin();p!=liu.end();p++){
        if(p==(liu.end()-1))
            line(gray,(*p),(*liu.begin()),Scalar(0,0,255),2,8,0);
        else
            line(gray,(*p),(*(p+1)),Scalar(0,0,255),2,8,0);
    }
	imshow("liu_add", gray);
    */


	waitKey(0);
	return 0;
}

/*
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
