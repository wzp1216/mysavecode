#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include <iostream>



int main(int argc, char** argv)
{
    cv::namedWindow("example",cv::WINDOW_AUTOSIZE);
    cv::VideoCapture cap;
    cap.open(std::string(argv[1]));
    cv::Mat frame;
    for(;;){
        cap>>frame;
        if(frame.empty()) break;
        cv::imshow("example",frame);
        if(cv::waitKey(33)>=0) break;
    }


    return 0;
}

