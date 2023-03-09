#include <QApplication>
#include "mainwindow.h"

int main(int argc,char *argv[]){
    QApplication app(argc,argv);
    MainWindow win;
    win.setWindowTitle("Qtopencv");
    win.show();
    return app.exec();
}

