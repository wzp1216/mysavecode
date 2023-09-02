qt first:
edit cpp file;
qmake -project -o aaa.pro //生成PRO
qmake                     //生成MAKEFILE
make                      //生成可执行文件
如提示 QApplication 找不到；在pro最后加一句
QT += widgets
############################################################
#include "mainwindow.h"
#include <QApplication>
#include <QMainWindow>
#include <QLabel>
int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    QLabel *lab1=new QLabel("hell qt!");
    lab1->show();
    //MainWindow w;
    //w.show();
    return a.exec();
}
可以使用HTML样式
    QLabel *lab1=new QLabel("<h2><i>Hello</i><font color=red>QT!</font></h2>");
############################################################
    QPushButton *button=new QPushButton("Quit");
    QObject::connect(button,SIGNAL(clicked()),&a,SLOT(quit()));
    button->show();
connect:button  clicked()---->a SLOT(quit())
############################################################
 QApplication a(argc, argv);
    QWidget *win=new QWidget;
    win->setWindowTitle("enter age");
    QSpinBox *spinbox=new QSpinBox;
    QSlider  *slider=new QSlider(Qt::Horizontal);
    spinbox->setRange(0,150);
    slider->setRange(0,150);

    QObject::connect(spinbox,SIGNAL(valueChanged(int)),
                     slider,SLOT(setValue(int)));
    QObject::connect(slider,SIGNAL(valueChanged(int)),
                     spinbox,SLOT(setValue(int)));
    spinbox->setValue(20);

    QHBoxLayout *lay=new QHBoxLayout;
    lay->addWidget(spinbox);
    lay->addWidget(slider);
    win->setLayout(lay);
    win->show();
两个控件，信号关联；
    connect(sender,SIGNAL(singnal),receiver,SLOT(slot));
    sender,reveiver是指向QObject的指针；
    singal slot是不带参数的函数名；
    发射信号时，会调用相对应的槽函数；
    要把信号成功连接到槽，两个函数必须具有相同的参数类型与顺序；
##################################################

FindDlg::FindDlg(QWidget *parent)
    :QDialog(parent)
{
    label=new QLabel("Find &what");
    lineedit=new QLineEdit;
    label->setBuddy(lineedit);

    caseCheckBox=new QCheckBox("Match &case");
    backwardCheckBox=new QCheckBox("search &backward");
    findButton=new QPushButton(tr("&find"));
    findButton->setDefault(true);
    findButton->setEnabled(false);
    closeButton=new QPushButton(tr("close"));

    connect(lineedit,SIGNAL(textChanged(const QString &)),
           this,SLOT(enableFindButton(const QString &)));
    connect(findButton,SIGNAL(clicked()),
            this,SLOT(findClicked()));
    connect(closeButton,SIGNAL(clicked()),
            this,SLOT(close()));

    QHBoxLayout *topleftlay=new QHBoxLayout;
    topleftlay->addWidget(label);
    topleftlay->addWidget(lineedit);
    QVBoxLayout *leftlay=new QVBoxLayout;
    leftlay->addLayout(topleftlay);
    leftlay->addWidget(caseCheckBox);
    leftlay->addWidget(backwardCheckBox);
    QVBoxLayout *rightlay=new QVBoxLayout;
    rightlay->addWidget(findButton);
    rightlay->addWidget(closeButton);
    rightlay->addStretch();
    QHBoxLayout *mainlay=new QHBoxLayout;
    mainlay->addLayout(leftlay);
    mainlay->addLayout(rightlay);
    setLayout(mainlay);
    setWindowTitle("Find");
    setFixedHeight(sizeHint().height());
}
void FindDlg::findClicked()
{
    QString text=lineedit->text();
    Qt::CaseSensitivity cs=
            caseCheckBox->isChecked()?Qt::CaseSensitive:Qt::CaseInsensitive;
    if (backwardCheckBox->isChecked()){
        emit findPrev(text,cs);
    }
    else{
        emit findNext(text,cs);
    }
}

void FindDlg::enableFindButton(const QString &text)
{
    qDebug()<<text.toUtf8()<<endl;
    findButton->setEnabled(!text.isEmpty());
}

findDlg类，其中添加了BUTTON LINEEDIT 并进行了布局；
其中出错误在 connect 时函数名 textChange  少了个字母 txtChange;
结果没有错误提示；不进入信号处理函数；增加
qDebug()后调试发现错误；
############################################################
OPENCV add pro file:
INCLUDEPATH += /usr/local/include/opencv4 \
                /usr/local/include/opencv4/opencv2

LIBS += /usr/local/lib/libopencv_* \

mainwindow add button ;add label ;read file and show image in label

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    connect(ui->pushButton,SIGNAL(clicked()),this,SLOT(show_file()));
}

void MainWindow::show_file()
{
    QString filename=QFileDialog::getOpenFileName(this,"open_image","/home/wzp/lena.jpg","Images (*.png *.jpg)");
    if (!filename.isEmpty()){
       cv::Mat  srcImage=cv::imread(filename.toStdString());
       if(!srcImage.empty()){
           cv::cvtColor(srcImage,srcImage,cv::COLOR_BGR2RGB);
           QImage image(srcImage.data, srcImage.cols,srcImage.rows,static_cast<int>(srcImage.step),QImage::Format_RGB888);
           ui->label->setPixmap(QPixmap::fromImage(image));
           ui->label->setScaledContents(true);
           ui->label->setSizePolicy(QSizePolicy::Ignored,QSizePolicy::Ignored);
       }
    }
}
点击BUTTON可以打开图片，并显示在LABEL中；
#########################################################

