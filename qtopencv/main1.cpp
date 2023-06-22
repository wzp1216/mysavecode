#include <opencv2/opencv.hpp>
#include <QtWidgets/QApplication>
#include <QtWidgets/QLabel>

int main(int argc,char** argv){
    QApplication a(argc,argv);
    cv::Mat img=cv::imread("./image/lena.jpg");

    QImage qimg(img.data,img.cols,img.rows,img.step,QImage::Format_RGB888);

    QLabel label1;
    label1.setPixmap(QPixmap::fromImage(qimg));
    label1.show();
    return  a.exec();


}

