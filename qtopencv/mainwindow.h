#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include<QMainWindow>
#include<QMenuBar>
#include<QToolBar>
#include<QAction>
#include<QGraphicsScene>
#include<QStatusBar>
#include<QLabel>
#include<QGraphicsPixmapItem>

class MainWindow : public QMainWindow
{
    Q_OBJECT
public:
    explicit MainWindow(QWidget *parent=nullptr);
    ~MainWindow();
private:
    void initUI();

};


#endif // MAINWINDOW_H
