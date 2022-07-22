#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include <iostream>
#include <fstream>

using namespace std;

int g_slider_position=0;
int g_run=1, g_set=0;
cv::VideoCapture g_cap;

void onTrackbarSlide(int pos,void *){
    g_cap.set(cv::CAP_PROP_POS_FRAMES,pos);
    if(g_set) g_run=1;
    g_set=1;
}

int main(int argc, char** argv)
{
    cv::namedWindow("example",cv::WINDOW_AUTOSIZE);
    g_cap.open(std::string(argv[1]));
    int frames=(int) g_cap.get(cv::CAP_PROP_FRAME_COUNT);
    int tmpw=(int) g_cap.get(cv::CAP_PROP_FRAME_WIDTH);
    int tmph=(int) g_cap.get(cv::CAP_PROP_FRAME_HEIGHT);
    cout<<"video has "<<frames<< " frames of dimesions("<<tmpw<<" X "<<tmph<<")."<<endl;
    cv::createTrackbar("Position","example",&g_slider_position,frames,onTrackbarSlide);

    cv::Mat frame;
    for(;;){
        if(g_run !=0) {
            g_cap>>frame;
            if(frame.empty()) break;
            int current_pos=(int)g_cap.get(cv::CAP_PROP_POS_FRAMES);
            g_set=0;

            cv::setTrackbarPos("Position","example",current_pos);
            cv::imshow("example",frame);
            g_run=1;
        }
    char c=(char) cv::waitKey(10);
    if(c=='s')
    {g_run=0;cout<<"stop play, run= "<<g_run<<endl;}
    if(c=='r')
    {g_run=1;cout<<"run step,run= "<<g_run<<endl;}
    if(c==27)
    {cv::destroyWindow("example");break;}
    }

    return 0;
}

