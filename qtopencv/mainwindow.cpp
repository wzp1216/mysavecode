#include<QApplication>
#include<QFileDialog>
#include<QMessageBox>
#include<QPixmap>
#include<QKeyEvent>
#include<QDebug>
#include"mainwindow.h"

MainWindow::MainWindow(QWidget *parent):
    QMainWindow(parent)
{
    initUI();
}

MainWindow::~MainWindow()
{

}

void MainWindow::initUI()
{
    this->resize(800,600);

}
