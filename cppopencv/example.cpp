#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;

int main(){
    Mat img;
    img=imread("./test.jpg");
    imshow("test",img);
    waitKey(0);
    

    return 0;

}
