#include "mainwindow.h"
#include <QApplication>
#include <QDir>
#include <QDebug>
#include <iostream>
#include <opencv2/opencv.hpp>

using namespace std;


void testimshow()
{
    try{
        QString mydir,myfile;
        mydir=QDir::currentPath();
        myfile=mydir.append("./image/lena.jpg");
        qDebug()<<myfile.toStdString().data();
        cv::Mat img;
        //img=cv::imread("/home/wzp/git/mysavecode/qtopencv/image/lena.jpg");
        img=cv::imread(myfile.toStdString().data());
        cv::namedWindow("win",cv::WINDOW_AUTOSIZE);
        cv::imshow("win",img);
        cv::waitKey(0);
        cv::destroyAllWindows();
    }
    catch (...){
        qDebug()<<"file read error ";
    }
}



int main(int argc, char *argv[])
{
    testimshow();
    return 0;
    //QApplication a(argc, argv);
    //MainWindow w;
    //w.show();
    //return a.exec();
}

