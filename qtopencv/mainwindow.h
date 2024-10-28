#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include<QMainWindow>
#include<QMenuBar>
#include<QToolBar>
#include<QAction>
#include<QGraphicsScene>
#include<QStatusBar>
#include<QPushButton>
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
    QWidget *dlg=new QWidget(this);
    QPushButton* but1=new QPushButton("OpenFile");
    QLabel* lab1=new QLabel("ShowImage");
private slots:
    void openfile();
};


#endif // MAINWINDOW_H
