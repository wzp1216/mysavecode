#include "opencv2/core.hpp"
#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;

int main(int argc, char** argv)
{
    try {
        Mat img=imread(argv[1],-1);
        if (img.empty()) return -1;
        namedWindow("example",cv::WINDOW_AUTOSIZE);
        imshow("example",img);
        cv::waitKey(0);
        cv::destroyWindow("example");
    }
    catch (...){
        cout<<"error no filename "<<endl;
    }

    return 0;
}

