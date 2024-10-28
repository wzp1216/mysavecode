#include <opencv2/opencv.hpp>
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>

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
		cout << "��ȷ��ͼ���ļ������Ƿ���ȷ" << endl;
		return -1;
	}
	GaussianBlur(gray, gray, Size(3, 3), 10, 10);  //ƽ���˲�
	vector<Vec3f> circles;
	double dp = 2; //
	double minDist = 20;  //����Բ��֮�����С����
	double	param1 = 50;  //Canny��Ե������ֵ
	double	param2 = 60;  //�ۼ�����ֵ
	int min_radius = 10;  //Բ�ΰ뾶����Сֵ
	int max_radius = 30;  //Բ�ΰ뾶�����ֵ
	HoughCircles(gray, circles, HOUGH_GRADIENT, dp, minDist, param1, param2,min_radius, max_radius);
	//111ͼ�����ҳ�Բ��
    int sum=0;
    int circle_number=circles.size();  
    if (circle_number!=0) 
        cout<<"find circles:"<<circle_number<<endl;
    else return 0;
    float radius_avg=0;
    vector<Point> cpoints;  //Բ��
	//222ͼ��Բ
    for (size_t i = 0; i < circles.size(); i++)	{
		Point center(cvRound(circles[i][0]), cvRound(circles[i][1]));
        cpoints.push_back(center);
	    float 	radius = circles[i][2];
        sum+=radius;
		circle(gray, center, cvRound(radius), Scalar(0, 0, 255), -1, 8, 0);
	}
    if (circle_number!=0) radius_avg=sum/circle_number;  //����ƽ���뾶
	imshow("img", gray);
	//333 �ҳ��ڽ�Բ
    Mat bin_gray;
    threshold(gray,bin_gray,10,255,THRESH_BINARY);
    Point2f key_center;   //����
    float big_radius=0;    
    minEnclosingCircle(cpoints,key_center,big_radius);  //��С�ڽ�Բ��������;
    circle(bin_gray,key_center,cvRound(big_radius),Scalar(0,0,255),2,LINE_AA);
	for (auto p=cpoints.begin();p!=cpoints.end();p++){
        if(getDistance((*p),key_center)>15*radius_avg)
            cpoints.erase(p);
        else
            circle(bin_gray,*p,cvRound(radius_avg),Scalar(0,0,255),2,LINE_AA);
	}
	//imshow("cir_add", bin_gray);
	//444 �ҳ�������
    vector<float> dist;  
    vector<Point> liu;  
	for (auto p:cpoints){
        dist.push_back(getDistance((p),key_center));
    }
    sort(dist.begin(),dist.end());
    float min_dist=*(dist.end()-7);
	for (auto p:cpoints){
        if ((getDistance((p),key_center)-min_dist)>0.001)
            liu.push_back(p);
    }
    cout<<"fonund key point:"<<liu.size()<<endl;
	for (auto p:liu){
        line(bin_gray,p,key_center,Scalar(0,0,255),6,8,0);
    }
	//imshow("liu_add",bin_gray);
    //555����ÿ��ֱ����ˮƽֱ�ߵĽǶ�
    float jiao[6];
    for (unsigned int i = 0; i<6; i++)  {
        float k=0; //ֱ��б��
        float x1,y1,x2,y2;
        x1=key_center.x;y1=key_center.y;
        x2=liu[i].x;y2=liu[i].y;
        if((x2>=x1)&&(y2<=y1)){
            k =(y1-y2)/(x2-x1);
            jiao[i]=atan(k)*180/CV_PI;
        }   
        else if((x2<x1)&&(y2<=y1)){
            k =(y1-y2)/(x1-x2);
            jiao[i]=180-atan(k)*180/CV_PI;
        }   
        else if((x2<x1)&&(y2>y1)){
            k =(y2-y1)/(x1-x2);
            jiao[i]=180+atan(k)*180/CV_PI;
        }   
        else if((x2>=x1)&&(y2>y1)){
            k =(y2-y1)/(x2-x1);
            jiao[i]=360-atan(k)*180/CV_PI;
        }   
    }
    vector<float> vjiao;
    for (unsigned int i=0; i<6; i++)  {
        vjiao.push_back(jiao[i]);
    }
    sort(vjiao.begin(),vjiao.end());
        //666��֤6�����ֵ�ǲ���60
    vector<float> cha;
    for(auto it=vjiao.begin()+1;it!=vjiao.end()-2;it++){
        float cha1=*(it)-*(it-1);
        float cha2=*(it+1)-*it;
        cha.push_back(fabs(cha1)+fabs(cha2));
    }
    for(auto it:vjiao) {
        it=cvRound(it*100)/100.0;
        cout<<it<<endl; }
    int min_pos=min_element(cha.begin(),cha.end())-cha.begin();
    stringstream ss;
    string textout;
    ss.clear();
    if(min_pos==0)  ss<<*vjiao.begin();
    else if(min_pos==1)  ss<<*(vjiao.begin()+1)-60;
    else if(min_pos==2)  ss<<*(vjiao.begin()+2)-120;
    else if(min_pos==3)  ss<<*(vjiao.begin()+3)-180;
    else ss<<"error";
    ss>>textout;
    Point pp(20,60);
    putText(bin_gray,textout,pp,FONT_HERSHEY_SIMPLEX,1,Scalar(0,0,0),3,8,0);
	imshow("liu_add",bin_gray);

    


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
