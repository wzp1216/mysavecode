import cv2
import json
import numpy as np
from PIL import Image

global h_min, h_max, s_min, s_max, v_min, v_max, blur, logyex, area


# 滑动条的回调函数，获取滑动条位置处的值
def empty(a):
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    blur = cv2.getTrackbarPos("blur", "TrackBars")
    logyex = cv2.getTrackbarPos("logyex", "TrackBars")
    area = cv2.getTrackbarPos("area", "TrackBars")
    # print(h_min, h_max, s_min, s_max, v_min, v_max,blur, logyex ,area)
    dicts = {'h_min': str(h_min),
             'h_max': str(h_max),
             's_min': str(s_min),
             's_max': str(s_max),
             'v_min': str(v_min),
             'v_max': str(v_max),
             'blur': str(blur),
             'logyex': str(logyex),
             'area': str(area)
             }
    json_str = json.dumps(dicts)
    with open('./paraments/tool_values.json', 'w') as json_file:
        json_file.write(json_str)
    json_file.close()
    return h_min, h_max, s_min, s_max, v_min, v_max, blur, logyex, area


with open('./paraments/tool_paraments.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)
# path = data['filename']
size = data['size']
path = "C:/Users/Administrator/MVS/Data/Image_18.jpg"
# 创建一个窗口，放置6个滑动条
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 500, 400)

cv2.createTrackbar("Hue Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("blur", "TrackBars", 1, 100, empty)
cv2.createTrackbar("logyex", "TrackBars", 1, 20, empty)
cv2.createTrackbar("area", "TrackBars", 1, 600, empty)
while True:
    img = cv2.imread(path)  # 143.png
    # img = 255 - img
    a = img.shape
    img = cv2.resize(img, (int(a[1] / int(2)), int(a[0] / int(2))), interpolation=cv2.INTER_CUBIC)
    # imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # 调用回调函数，获取滑动条的值
    h_min, h_max, s_min, s_max, v_min, v_max, blur, logyex, area = empty(0)
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
    # 提取连通域
    _, labels, stats, centroids = cv2.connectedComponentsWithStats(canny_binary_black, connectivity=8)
    i = 0
    for istat in stats:
        if istat[4] < area:
            # print(i)
            print(istat[0:2])
            if istat[3] > istat[4]:
                r = istat[3]
            else:
                r = istat[4]
            cv2.rectangle(canny_binary_black, tuple(istat[0:2]), tuple(istat[0:2] + istat[2:4]), 0, thickness=-1)  # 26
        i = i + 1
    # 绘制轮廓
    _, contours, _ = cv2.findContours(canny_binary_black, cv2.RETR_EXTERNAL,
                                      cv2.CHAIN_APPROX_NONE)  # 输出所有轮廓cv2.RETR_TREE，
    # cv2.drawContours(img, contours, -1, (0, 0, 255), -1)
    for i in range(0, len(contours)):
        x, y, w, h = cv2.boundingRect(contours[i])
        cv2.rectangle(img, (x, y), (x + w, y + h), (128, 0, 0), 2)

    cv2.imshow("img", img)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", mask_blac)
    cv2.waitKey(1)
