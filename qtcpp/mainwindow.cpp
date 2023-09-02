#include "mainwindow.h"
#include "ui_mainwindow.h"

#include <iostream>
#include <QFileDialog>
#include <QImage>
#include <QPixmap>

#include <opencv2/opencv.hpp>
#include <opencv2/core.hpp>

using namespace cv;

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::Button_clicked()
{
 std::cout << "test_ "<< std::endl;

// Mat srcImage;
// srcImage = imread("1.png");
// imshow("photo", srcImage);
// waitKey();
// getchar();


 QString fileName = QFileDialog::getOpenFileName(this, "Open Image", "", "Images (*.png *.jpg)");

 if (!fileName.isEmpty()) {
     // 从选定的文件加载图像
     cv::Mat srcImage = cv::imread(fileName.toStdString());

     if (!srcImage.empty()) {
         // 将颜色空间从BGR转换为RGB
         cv::cvtColor(srcImage, srcImage, cv::COLOR_BGR2RGB);

         // 将图像显示到 QLabel 上

         QImage image(srcImage.data, srcImage.cols, srcImage.rows, static_cast<int>(srcImage.step),QImage::Format_RGB888);
         ui->label->setPixmap(QPixmap::fromImage(image));

         // 调整 QLabel 的大小以适应图像
         ui->label->setScaledContents(true);
         ui->label->setSizePolicy(QSizePolicy::Ignored, QSizePolicy::Ignored);
     }
 }

}
