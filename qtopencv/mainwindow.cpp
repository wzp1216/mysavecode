#include<QApplication>
#include<QFileDialog>
#include<QMessageBox>
#include<QPushButton>
#include<QPixmap>
#include<QKeyEvent>
#include<QDebug>
#include<QVBoxLayout>
#include"mainwindow.h"
#include <opencv2/opencv.hpp>

MainWindow::MainWindow(QWidget *parent):
    QMainWindow(parent)
{
    initUI();
    connect(this->but1,SIGNAL(clicked()),this,SLOT(openfile()));
}
void MainWindow::openfile()
{
    QString filename=QFileDialog::getOpenFileName(this,"open_image","/home/wzp/lena.jpg","Images (*.png *.jpg)");
        if (!filename.isEmpty()){
           cv::Mat  srcImage=cv::imread(filename.toStdString());
           if(!srcImage.empty()){
               cv::cvtColor(srcImage,srcImage,cv::COLOR_BGR2RGB);
               QImage image(srcImage.data, srcImage.cols,srcImage.rows,static_cast<int>(srcImage.step),QImage::Format_RGB888);
               this->lab1->setPixmap(QPixmap::fromImage(image));
               this->lab1->setScaledContents(true);
               this->lab1->setSizePolicy(QSizePolicy::Ignored,QSizePolicy::Ignored);
           }
        }

}

void MainWindow::initUI()
{
    this->resize(800,600);
    QVBoxLayout* toplay= new QVBoxLayout;
    toplay->addWidget(this->but1);
    toplay->addWidget(this->lab1);
    dlg->setLayout(toplay);
    dlg->setMinimumSize(400,400);
    this->setCentralWidget(this->dlg);
}

MainWindow::~MainWindow()
{
}
