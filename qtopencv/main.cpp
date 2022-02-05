#include "mainwindow.h"
#include <QApplication>
#include <QDir>
#include <iostream>
#include <opencv2/opencv.hpp>

using namespace std;
/*
int main(int argc, char *argv[])
{
    Mat image;
    char keyPress;
    cout<<"Welcome to Qt\n";
    image=imread("./lena.jpg",IMREAD_COLOR);
    imshow("Opnecv && QT",image);
    while (1) {
        keyPress=waitKey();
        if(keyPress=='q')
        {
            destroyAllWindows();
            break;
        }
    }
    return 0;
}
*/
int main(int argc, char *argv[])
{
    try{
        QString mydir,myfile;
        mydir=QDir::currentPath();
        myfile=mydir.append("/../qtopencv/image/lena.jpg");
        cout<<myfile.toStdString().data()<<endl;
        cv::Mat img;
        //img=cv::imread("/home/wzp/git/mysavecode/qtopencv/image/lena.jpg");
        img=cv::imread(myfile.toStdString().data());
        cv::namedWindow("win",cv::WINDOW_AUTOSIZE);
        cv::imshow("win",img);
        cv::waitKey(0);
        cv::destroyAllWindows();
    }
    catch (...){
        cout<<"file read error "<<endl;
    }
    return 0;
    //QApplication a(argc, argv);
    //MainWindow w;
    //w.show();

    //return a.exec();
}

