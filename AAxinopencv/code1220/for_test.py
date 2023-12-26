import cv2
import json
import numpy as np

global h_min, h_max, s_min, s_max, v_min, v_max, min_size, blur, logyex

# 滑动条的回调函数，获取滑动条位置处的值
def empty(a):
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    min_size = cv2.getTrackbarPos("Min Size", "TrackBars")
    blur = cv2.getTrackbarPos("blur", "TrackBars")
    logyex = cv2.getTrackbarPos("logyex", "TrackBars")

    dicts = {'h_min': str(h_min),
             'h_max': str(h_max),
             's_min': str(s_min),
             's_max': str(s_max),
             'v_min': str(v_min),
             'v_max': str(v_max),
             'blur': str(blur),
             'logyex': str(logyex),
             'min_size': str(min_size)
             }
    json_str = json.dumps(dicts)
    with open('./paraments/tool_values.json', 'w') as json_file:
        json_file.write(json_str)
    json_file.close()
    min_size = float(0.01 * min_size)
    return h_min, h_max, s_min, s_max, v_min, v_max, min_size, blur, logyex

# 滑动条的回调函数，获取滑动条位置处的值
def empty1(a):
    global blocksize
    global c
    blocksize = cv2.getTrackbarPos("blocksize", "TrackBars")
    c = cv2.getTrackbarPos("c", "TrackBars")
    min_size = cv2.getTrackbarPos("min size", "TrackBars")
    print(blocksize, c)
    dicts = {'blocksize': str(blocksize+1),
             'c': str(c)
             }
    json_str = json.dumps(dicts)
    with open('./paraments/tool_values.json', 'w') as json_file:
        json_file.write(json_str)
    json_file.close()
    min_size = float(0.01 * min_size)
    c = float(0.1 * c)
    return blocksize, c, min_size

with open('./paraments/tool_paraments.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)
# path = data['filename']
size = data['size']
threshold = data['threshold']
sample = data['sample']
original = './paraments/original.jpg'
if sample == 'sample1' or sample == 'sample2':
    f = open('./paraments/label.txt')
    label = f.readline()
    if int(label) == 0 or int(label) == 1:
        path = './paraments/result.jpg'
        # 创建一个窗口，放置6个滑动条
        if threshold == 'global':
            cv2.namedWindow("TrackBars")
            cv2.resizeWindow("TrackBars", 500, 400)
            cv2.createTrackbar("Hue Min", "TrackBars", 0, 255, empty)
            cv2.createTrackbar("Hue Max", "TrackBars", 255, 255, empty)
            cv2.createTrackbar("Sat Min", "TrackBars", 0, 255, empty)
            cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
            cv2.createTrackbar("Val Min", "TrackBars", 0, 255, empty)
            cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)
            cv2.createTrackbar("Min Size", "TrackBars", 0, 500, empty)
            cv2.createTrackbar("blur", "TrackBars", 1, 100, empty)
            cv2.createTrackbar("logyex", "TrackBars", 1, 20, empty)
            while True:
                img0 = cv2.imread(original)
                img0 = cv2.resize(img0, (int(img0.shape[1] / int(size)), int(img0.shape[0] / int(size))),
                                  interpolation=cv2.INTER_CUBIC)
                img = cv2.imread(path) #143.png
                # img = 255 - img
                a = img.shape
                img = cv2.resize(img, (int(a[1]/int(size)), int(a[0]/int(size))), interpolation=cv2.INTER_CUBIC)
                # imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
                # 调用回调函数，获取滑动条的值
                h_min, h_max, s_min, s_max, v_min, v_max, min_size, blur, logyex= empty(0)
                lower = np.array([h_min, s_min, v_min])
                upper = np.array([h_max, s_max, v_max])
                img_blur = cv2.blur(imgHSV, (blur, blur))
                # img_blur = cv2.bilateralFilter(imgHSV, 9, blur, blur)
                # 获得指定颜色范围内的掩码
                mask = cv2.inRange(img_blur, lower, upper)
                # 对原图图像进行按位与的操作，掩码区域保留
                mask_blac = cv2.bitwise_and(img, img, mask=mask)
                # 设置卷积核
                kernel = np.ones((logyex, logyex), np.uint8)
                # 图像闭运算
                imglogyex = cv2.morphologyEx(mask_blac, cv2.MORPH_CLOSE, kernel)
                #二值化
                ret, threshold_binary_black = cv2.threshold(imglogyex, 0, 255, cv2.THRESH_BINARY_INV)
                #边缘检测
                canny_binary_black = cv2.Canny(threshold_binary_black, 0, 10, apertureSize=3)
                # 绘制轮廓
                _, contours, _ = cv2.findContours(canny_binary_black, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)   # 输出所有轮廓cv2.RETR_TREE，
                cntArea = []
                # min_size = float(min_size * 0.1)
                if contours is not None:
                    for i in range(len(contours)):
                        area = cv2.contourArea(contours[i])
                        if area >= min_size:
                            cntArea.append(contours[i])
                cv2.drawContours(img0, cntArea, -1, (0, 0, 255), 1)
                cv2.imshow("img",img)
                cv2.imshow("Mask", mask)
                cv2.imshow("Result", img0)
                cv2.waitKey(1)
        if threshold == 'adaptive':
            cv2.namedWindow("TrackBars")
            cv2.resizeWindow("TrackBars", 500, 150)
            cv2.createTrackbar("blocksize", "TrackBars", 3, 699, empty)
            cv2.createTrackbar("c", "TrackBars", 1, 300, empty)
            cv2.createTrackbar("min size", "TrackBars", 0, 500, empty)
            while True:
                img0 = cv2.imread(original)
                img0 = cv2.resize(img0, (int(img0.shape[1] / int(size)), int(img0.shape[0] / int(size))),
                                  interpolation=cv2.INTER_CUBIC)
                img = cv2.imread(path) #143.png
                # img = 255 - img
                a = img.shape
                img = cv2.resize(img, (int(a[1]/int(size)), int(a[0]/int(size))), interpolation=cv2.INTER_CUBIC)
                imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                blocksize, c, min_size = empty1(0)
                if blocksize % 2 == 0:
                    blocksize = blocksize + 1
                else:
                    blocksize = blocksize
                dst = cv2.adaptiveThreshold(imggray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, blocksize, c)
                _, contours, _ = cv2.findContours(dst, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
                cntArea = []
                # min_size = float(min_size * 0.1)
                if contours is not None:
                    for i in range(len(contours)):
                        area = cv2.contourArea(contours[i])
                        if area >= min_size:
                            cntArea.append(contours[i])

                cv2.drawContours(img0, cntArea, -1, [0, 0, 255], 1)

                cv2.imshow('img', img)
                cv2.imshow('adaptive img', dst)
                cv2.imshow('result', img0)
                cv2.waitKey(1)
        if threshold == 'local':
            cv2.namedWindow("TrackBars")
            cv2.resizeWindow("TrackBars", 500, 150)
            cv2.createTrackbar("blocksize", "TrackBars", 3, 699, empty)
            cv2.createTrackbar("c", "TrackBars", 0, 300, empty)
            cv2.createTrackbar("min size", "TrackBars", 0, 500, empty)
            while True:
                img0 = cv2.imread(original)
                img0 = cv2.resize(img0, (int(img0.shape[1] / int(size)), int(img0.shape[0] / int(size))), interpolation=cv2.INTER_CUBIC)
                img = cv2.imread(path) #143.png
                # img = 255 - img
                a = img.shape
                img = cv2.resize(img, (int(a[1]/int(size)), int(a[0]/int(size))), interpolation=cv2.INTER_CUBIC)
                imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                blocksize, c, min_size = empty1(0)
                if blocksize % 2 == 0:
                    blocksize = blocksize + 1
                else:
                    blocksize = blocksize
                dst = cv2.ximgproc.niBlackThreshold(imggray, 255, cv2.THRESH_BINARY, blocksize, c, cv2.THRESH_BINARY, cv2.ximgproc.BINARIZATION_NIBLACK)
                _, contours, _ = cv2.findContours(dst, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
                cntArea = []
                # min_size = float(min_size * 0.1)
                if contours is not None:
                    for i in range(len(contours)):
                        area = cv2.contourArea(contours[i])
                        if area >= min_size:
                            cntArea.append(contours[i])

                cv2.drawContours(img0, cntArea, -1, [0, 0, 255], 1)
                cv2.imshow('img', img)
                cv2.imshow('local img', dst)
                cv2.imshow('result', img0)
                cv2.waitKey(1)
if sample == 'sample3' or sample == 'sample4':
    f = open('./paraments/label.txt')
    label = f.readline()
    if int(label) == 0:
        path1 = './paraments/result1.jpg'
        path2 = './paraments/result2.jpg'
        # 创建一个窗口，放置6个滑动条
        if threshold == 'global':
            cv2.namedWindow("TrackBars")
            cv2.resizeWindow("TrackBars", 500, 400)
            cv2.createTrackbar("Hue Min", "TrackBars", 0, 255, empty)
            cv2.createTrackbar("Hue Max", "TrackBars", 255, 255, empty)
            cv2.createTrackbar("Sat Min", "TrackBars", 0, 255, empty)
            cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
            cv2.createTrackbar("Val Min", "TrackBars", 0, 255, empty)
            cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)
            cv2.createTrackbar("Min Size", "TrackBars", 0, 500, empty)
            cv2.createTrackbar("blur", "TrackBars", 1, 100, empty)
            cv2.createTrackbar("logyex", "TrackBars", 1, 20, empty)
            while True:
                img0 = cv2.imread(original)
                img0 = cv2.resize(img0, (int(img0.shape[1] / int(size)), int(img0.shape[0] / int(size))),
                                  interpolation=cv2.INTER_CUBIC)
                img1 = cv2.imread(path1)  # 143.png
                # img = 255 - img
                a = img1.shape
                img1 = cv2.resize(img1, (int(a[1] / int(size)), int(a[0] / int(size))), interpolation=cv2.INTER_CUBIC)
                # imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                img1HSV = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
                # 调用回调函数，获取滑动条的值
                h_min, h_max, s_min, s_max, v_min, v_max, min_size, blur, logyex = empty(0)
                lower = np.array([h_min, s_min, v_min])
                upper = np.array([h_max, s_max, v_max])
                img1_blur = cv2.blur(img1HSV, (blur, blur))
                # img_blur = cv2.bilateralFilter(imgHSV, 9, blur, blur)
                # 获得指定颜色范围内的掩码
                mask1 = cv2.inRange(img1_blur, lower, upper)
                # 对原图图像进行按位与的操作，掩码区域保留
                mask_blac1 = cv2.bitwise_and(img1, img1, mask=mask1)
                # 设置卷积核
                kernel = np.ones((logyex, logyex), np.uint8)
                # 图像闭运算
                imglogyex1 = cv2.morphologyEx(mask_blac1, cv2.MORPH_CLOSE, kernel)
                # 二值化
                ret, threshold_binary_black1 = cv2.threshold(imglogyex1, 0, 255, cv2.THRESH_BINARY_INV)
                # 边缘检测
                canny_binary_black1 = cv2.Canny(threshold_binary_black1, 0, 10, apertureSize=3)
                # 绘制轮廓
                _, contours1, _ = cv2.findContours(canny_binary_black1, cv2.RETR_EXTERNAL,
                                                  cv2.CHAIN_APPROX_NONE)  # 输出所有轮廓cv2.RETR_TREE，
                cntArea1 = []
                # min_size = float(min_size * 0.1)
                if contours1 is not None:
                    for i in range(len(contours1)):
                        area = cv2.contourArea(contours1[i])
                        if area >= min_size:
                            cntArea1.append(contours1[i])

                img2 = cv2.imread(path2)  # 143.png
                # img = 255 - img
                a = img2.shape
                img2 = cv2.resize(img2, (int(a[1] / int(size)), int(a[0] / int(size))), interpolation=cv2.INTER_CUBIC)
                # imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                img2HSV = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
                # 调用回调函数，获取滑动条的值
                h_min, h_max, s_min, s_max, v_min, v_max, min_size, blur, logyex = empty(0)
                lower = np.array([h_min, s_min, v_min])
                upper = np.array([h_max, s_max, v_max])
                img2_blur = cv2.blur(img2HSV, (blur, blur))
                # img_blur = cv2.bilateralFilter(imgHSV, 9, blur, blur)
                # 获得指定颜色范围内的掩码
                mask2 = cv2.inRange(img2_blur, lower, upper)
                # 对原图图像进行按位与的操作，掩码区域保留
                mask_blac2 = cv2.bitwise_and(img2, img2, mask=mask1)
                # 设置卷积核
                kernel = np.ones((logyex, logyex), np.uint8)
                # 图像闭运算
                imglogyex2 = cv2.morphologyEx(mask_blac2, cv2.MORPH_CLOSE, kernel)
                # 二值化
                ret, threshold_binary_black2 = cv2.threshold(imglogyex2, 0, 255, cv2.THRESH_BINARY_INV)
                # 边缘检测
                canny_binary_black2 = cv2.Canny(threshold_binary_black2, 0, 10, apertureSize=3)
                # 绘制轮廓
                _, contours2, _ = cv2.findContours(canny_binary_black2, cv2.RETR_EXTERNAL,
                                                   cv2.CHAIN_APPROX_NONE)  # 输出所有轮廓cv2.RETR_TREE，
                cntArea2 = []
                if contours2 is not None:
                    for i in range(len(contours2)):
                        area = cv2.contourArea(contours2[i])
                        if area >= min_size:
                            cntArea2.append(contours2[i])
                cv2.drawContours(img0, cntArea1, -1, (0, 0, 255), 1)
                cv2.drawContours(img0, cntArea2, -1, (0, 0, 255), 1)
                cv2.imshow("Result", img0)
                cv2.waitKey(1)
        if threshold == 'adaptive':
            cv2.namedWindow("TrackBars")
            cv2.resizeWindow("TrackBars", 500, 150)
            cv2.createTrackbar("blocksize", "TrackBars", 3, 699, empty)
            cv2.createTrackbar("c", "TrackBars", 1, 300, empty)
            cv2.createTrackbar("min size", "TrackBars", 0, 500, empty)
            while True:
                img0 = cv2.imread(original)
                img0 = cv2.resize(img0, (int(img0.shape[1] / int(size)), int(img0.shape[0] / int(size))),
                                  interpolation=cv2.INTER_CUBIC)
                img1 = cv2.imread(path1)  # 143.png
                # img = 255 - img
                a = img1.shape
                img1 = cv2.resize(img1, (int(a[1] / int(size)), int(a[0] / int(size))), interpolation=cv2.INTER_CUBIC)
                imggray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
                blocksize, c, min_size = empty1(0)
                if blocksize % 2 == 0:
                    blocksize = blocksize + 1
                else:
                    blocksize = blocksize
                dst1 = cv2.adaptiveThreshold(imggray1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, blocksize,
                                            c)
                _, contours1, _ = cv2.findContours(dst1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

                img2 = cv2.imread(path2)  # 143.png
                # img = 255 - img
                a = img2.shape
                img2 = cv2.resize(img2, (int(a[1] / int(size)), int(a[0] / int(size))), interpolation=cv2.INTER_CUBIC)
                imggray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
                blocksize, c, min_size= empty1(0)
                if blocksize % 2 == 0:
                    blocksize = blocksize + 1
                else:
                    blocksize = blocksize
                dst2 = cv2.adaptiveThreshold(imggray2, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,
                                             blocksize,
                                             c)
                _, contours2, _ = cv2.findContours(dst2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

                cntArea1 = []
                # min_size = float(min_size * 0.1)
                if contours1 is not None:
                    for i in range(len(contours1)):
                        area = cv2.contourArea(contours1[i])
                        if area >= min_size:
                            cntArea1.append(contours1[i])
                cntArea2 = []
                if contours2 is not None:
                    for i in range(len(contours2)):
                        area = cv2.contourArea(contours2[i])
                        if area >= min_size:
                            cntArea2.append(contours2[i])

                cv2.drawContours(img0, cntArea1, -1, [0, 0, 255], 1)
                cv2.drawContours(img0, cntArea2, -1, [0, 0, 255], 1)
                # cv2.imshow('img', img)
                # cv2.imshow('adaptive img', dst)
                cv2.imshow('result', img0)
                cv2.waitKey(1)
        if threshold == 'local':
            cv2.namedWindow("TrackBars")
            cv2.resizeWindow("TrackBars", 500, 150)
            cv2.createTrackbar("blocksize", "TrackBars", 3, 699, empty)
            cv2.createTrackbar("c", "TrackBars", 1, 300, empty)
            cv2.createTrackbar("min size", "TrackBars", 0, 500, empty)
            while True:
                img0 = cv2.imread(original)
                img0 = cv2.resize(img0, (int(img0.shape[1] / int(size)), int(img0.shape[0] / int(size))),
                                  interpolation=cv2.INTER_CUBIC)
                img1 = cv2.imread(path1)  # 143.png
                # img = 255 - img
                a = img1.shape
                img1 = cv2.resize(img1, (int(a[1] / int(size)), int(a[0] / int(size))), interpolation=cv2.INTER_CUBIC)
                imggray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
                blocksize, c, min_size = empty1(0)
                if blocksize % 2 == 0:
                    blocksize = blocksize + 1
                else:
                    blocksize = blocksize
                dst1 = cv2.ximgproc.niBlackThreshold(imggray1, 255, cv2.THRESH_BINARY, blocksize, c, cv2.THRESH_BINARY,
                                                    cv2.ximgproc.BINARIZATION_NIBLACK)
                _, contours1, _ = cv2.findContours(dst1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

                img2 = cv2.imread(path2)  # 143.png
                # img = 255 - img
                a = img2.shape
                img2 = cv2.resize(img2, (int(a[1] / int(size)), int(a[0] / int(size))), interpolation=cv2.INTER_CUBIC)
                imggray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
                blocksize, c, min_size = empty1(0)
                if blocksize % 2 == 0:
                    blocksize = blocksize + 1
                else:
                    blocksize = blocksize
                dst2 = cv2.ximgproc.niBlackThreshold(imggray2, 255, cv2.THRESH_BINARY, blocksize, c, cv2.THRESH_BINARY,
                                                    cv2.ximgproc.BINARIZATION_NIBLACK)
                _, contours2, _ = cv2.findContours(dst2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

                cntArea1 = []
                # min_size = float(min_size * 0.1)
                if contours1 is not None:
                    for i in range(len(contours1)):
                        area = cv2.contourArea(contours1[i])
                        if area >= min_size:
                            cntArea1.append(contours1[i])
                cntArea2 = []
                if contours2 is not None:
                    for i in range(len(contours2)):
                        area = cv2.contourArea(contours2[i])
                        if area >= min_size:
                            cntArea2.append(contours2[i])
                cv2.drawContours(img0, cntArea1, -1, [0, 0, 255], 1)
                cv2.drawContours(img0, cntArea2, -1, [0, 0, 255], 1)
                # cv2.imshow('img', img)
                # cv2.imshow('local img', dst)
                cv2.imshow('result', img0)
                cv2.waitKey(1)
    else:
        path = './paraments/result.jpg'
        # 创建一个窗口，放置6个滑动条
        if threshold == 'global':
            cv2.namedWindow("TrackBars")
            cv2.resizeWindow("TrackBars", 500, 400)
            cv2.createTrackbar("Hue Min", "TrackBars", 0, 255, empty)
            cv2.createTrackbar("Hue Max", "TrackBars", 255, 255, empty)
            cv2.createTrackbar("Sat Min", "TrackBars", 0, 255, empty)
            cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
            cv2.createTrackbar("Val Min", "TrackBars", 0, 255, empty)
            cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)
            cv2.createTrackbar("Min Size", "TrackBars", 0, 500, empty)
            cv2.createTrackbar("blur", "TrackBars", 1, 100, empty)
            cv2.createTrackbar("logyex", "TrackBars", 1, 20, empty)
            while True:
                img0 = cv2.imread(original)
                img0 = cv2.resize(img0, (int(img0.shape[1] / int(size)), int(img0.shape[0] / int(size))),
                                  interpolation=cv2.INTER_CUBIC)
                img = cv2.imread(path)  # 143.png
                # img = 255 - img
                a = img.shape
                img = cv2.resize(img, (int(a[1] / int(size)), int(a[0] / int(size))), interpolation=cv2.INTER_CUBIC)
                # imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
                # 调用回调函数，获取滑动条的值
                h_min, h_max, s_min, s_max, v_min, v_max, min_size, blur, logyex = empty(0)
                lower = np.array([h_min, s_min, v_min])
                upper = np.array([h_max, s_max, v_max])
                img_blur = cv2.blur(imgHSV, (blur, blur))
                # img_blur = cv2.bilateralFilter(imgHSV, 9, blur, blur)
                # 获得指定颜色范围内的掩码
                mask = cv2.inRange(img_blur, lower, upper)
                # 对原图图像进行按位与的操作，掩码区域保留
                mask_blac = cv2.bitwise_and(img, img, mask=mask)
                # 设置卷积核
                kernel = np.ones((logyex, logyex), np.uint8)
                # 图像闭运算
                imglogyex = cv2.morphologyEx(mask_blac, cv2.MORPH_CLOSE, kernel)
                # 二值化
                ret, threshold_binary_black = cv2.threshold(imglogyex, 0, 255, cv2.THRESH_BINARY_INV)
                # 边缘检测
                canny_binary_black = cv2.Canny(threshold_binary_black, 0, 10, apertureSize=3)
                # 绘制轮廓
                _, contours, _ = cv2.findContours(canny_binary_black, cv2.RETR_EXTERNAL,
                                                  cv2.CHAIN_APPROX_NONE)  # 输出所有轮廓cv2.RETR_TREE，
                cntArea = []
                # min_size = float(min_size * 0.1)
                if contours is not None:
                    for i in range(len(contours)):
                        area = cv2.contourArea(contours[i])
                        if area >= min_size:
                            cntArea.append(contours[i])
                cv2.drawContours(img0, cntArea, -1, (0, 0, 255), 1)
                cv2.imshow("img", img)
                cv2.imshow("Mask", mask)
                cv2.imshow("Result", img0)
                cv2.waitKey(1)
        if threshold == 'adaptive':
            cv2.namedWindow("TrackBars")
            cv2.resizeWindow("TrackBars", 500, 150)
            cv2.createTrackbar("blocksize", "TrackBars", 3, 699, empty)
            cv2.createTrackbar("c", "TrackBars", 1, 300, empty)
            cv2.createTrackbar("min_size", "TrackBars", 0, 500, empty)
            while True:
                img0 = cv2.imread(original)
                img0 = cv2.resize(img0, (int(img0.shape[1] / int(size)), int(img0.shape[0] / int(size))),
                                  interpolation=cv2.INTER_CUBIC)
                img = cv2.imread(path)  # 143.png
                # img = 255 - img
                a = img.shape
                img = cv2.resize(img, (int(a[1] / int(size)), int(a[0] / int(size))), interpolation=cv2.INTER_CUBIC)
                imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                blocksize, c, min_size = empty1(0)
                if blocksize % 2 == 0:
                    blocksize = blocksize + 1
                else:
                    blocksize = blocksize
                dst = cv2.adaptiveThreshold(imggray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, blocksize,
                                            c)
                _, contours, _ = cv2.findContours(dst, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
                cntArea = []
                # min_size = float(min_size * 0.1)
                if contours is not None:
                    for i in range(len(contours)):
                        area = cv2.contourArea(contours[i])
                        if area >= min_size:
                            cntArea.append(contours[i])

                cv2.drawContours(img0, contours, -1, [0, 0, 255], 1)

                cv2.imshow('img', img)
                cv2.imshow('adaptive img', dst)
                cv2.imshow('result', img0)
                cv2.waitKey(1)
        if threshold == 'local':
            cv2.namedWindow("TrackBars")
            cv2.resizeWindow("TrackBars", 500, 150)
            cv2.createTrackbar("blocksize", "TrackBars", 3, 699, empty)
            cv2.createTrackbar("c", "TrackBars", 1, 300, empty)
            cv2.createTrackbar("min size", "TrackBars", 0, 500, empty)
            while True:
                img0 = cv2.imread(original)
                img0 = cv2.resize(img0, (int(img0.shape[1] / int(size)), int(img0.shape[0] / int(size))),
                                  interpolation=cv2.INTER_CUBIC)
                img = cv2.imread(path)  # 143.png
                # img = 255 - img
                a = img.shape
                img = cv2.resize(img, (int(a[1] / int(size)), int(a[0] / int(size))), interpolation=cv2.INTER_CUBIC)
                imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                blocksize, c, min_size = empty1(0)
                if blocksize % 2 == 0:
                    blocksize = blocksize + 1
                else:
                    blocksize = blocksize
                dst = cv2.ximgproc.niBlackThreshold(imggray, 255, cv2.THRESH_BINARY, blocksize, c, cv2.THRESH_BINARY,
                                                    cv2.ximgproc.BINARIZATION_NIBLACK)
                _, contours, _ = cv2.findContours(dst, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
                cntArea = []
                # min_size = float(min_size * 0.1)
                if contours is not None:
                    for i in range(len(contours)):
                        area = cv2.contourArea(contours[i])
                        if area >= min_size:
                            cntArea.append(contours[i])

                cv2.drawContours(img0, contours, -1, [0, 0, 255], 1)
                cv2.imshow('img', img)
                cv2.imshow('local img', dst)
                cv2.imshow('result', img0)
                cv2.waitKey(1)
