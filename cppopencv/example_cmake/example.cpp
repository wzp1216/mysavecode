#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;

int s_slider_position=0;
int g_run=0;
int g_dontset=0;
cv::VideoCapture g_cap;

void onTrackbarSlide(int pos , void *){
    g_cap.set(cv::CAP_PROP_POS_FRAMES,pos);
    if(!g_dontset) g_run=1;
    g_dontset=0;
}

int main(){
    cv::namedWindow("examp",cv::WINDOW_AUTOSIZE);

    return 0;

}
