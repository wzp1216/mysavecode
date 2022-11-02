#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include <iostream>
#include <QImage>
#include <QPixmap>
#include <opencv2/opencv.hpp>



unsing namespace cv;

int main(int argc, char** argv)
{
    Mat img = imread("../test.jpg");
    cv::cvtColor(img, img, cv::COLOR_BGR2RGB);
    QImage image = QImage((const unsigned char *)(img.data),img.cols,img.rows,img.step,QImage::Format_RGB888);
    ui->label->setPixmap(QPixmap::fromImage(image));
    ui->label->resize(image.size());
    ui->label->show();
    resize(800,500);
    

    return 0;
}

