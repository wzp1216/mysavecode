#ifndef MYCAMERA_H
#define MYCAMERA_H

#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include "MvCameraControl.h"
#include "opencv2/core/core.hpp"
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc.hpp"
#include <QDebug>
#include <QImage>

using namespace std;
using namespace cv;

class mycamera : public QObject
{
    Q_OBJECT
public:
    explicit mycamera(QObject *parent = nullptr);
    ~mycamera();
    void PrintDeviceInfo();
    void close_cam();
    void start_cam();
    void get_pic(Mat * srcimg);
    void re_iso();
    int  testcam();
private:
    void* handle;
    bool g_bExit;
    int nRet;
    unsigned int g_nPayloadSize;
    unsigned char *pDataForRGB;
    MV_CC_DEVICE_INFO* pDeviceInfo;
    MV_CC_DEVICE_INFO_LIST stDeviceList;
    MVCC_INTVALUE stParam;
    MV_FRAME_OUT stOutFrame;
    MV_CC_PIXEL_CONVERT_PARAM CvtParam;
};

#endif // MYCAMERA_H
