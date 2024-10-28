#include <opencv2/opencv.hpp>
#include <iostream>
using namespace cv;
int main(int argc, char** argv){
    Mat img=imread(argv[1],-1);
    if (img.empty()) return -1;
    namedWindow("example",cv::WINDOW_AUTOSIZE);
    imshow("example",img);
    waitKey(0);
    destroyWindow("example");
    return 0;
}
