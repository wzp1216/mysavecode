import cv2
import numpy as np


# # 获取roi区域
# def get_roi_large_cylinder(img):
#     """
#     此函数最终目的获取图像的roi区域，在此之前会进行滤波，开运算等操作
#     :param img: 读取的原图
#     :return: 返回只含有roi区域的图像
#     """
#     img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     # img_blur = cv2.blur(img_gray, (5, 5))  # 降噪滤波
#     # opening = cv2.morphologyEx(img_blur, cv2.MORPH_OPEN, (7, 7))  # 形态学开运算
#     # bila = cv2.bilateralFilter(opening, 10, 200, 200)  # 双边滤波消除噪声
#     t, dst = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
#     _, contours, _ = cv2.findContours(dst, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
#     mask = np.zeros(img.shape, np.uint8)
#
#     # 取出最大轮廓，进行roi提取
#     if len(contours) == 1:
#         mask_new = cv2.drawContours(mask, contours, -1, [255, 255, 255], -1)
#     else:
#         temp = []
#         for i in range(len(contours)):
#             temp.append(len(contours[i]))
#         theset = frozenset(temp)
#         theset = sorted(theset, reverse=True)
#         first_contours = contours[temp.index(theset[0])]
#         first_contours = [first_contours]
#         mask_new = cv2.drawContours(mask, first_contours, -1, [255, 255, 255], -1)
#     img_roi = cv2.bitwise_and(img, mask_new)
#     return img_roi, dst


def get_roi_large_cylinder(img):
    """
    此函数作用是获取同心圆圆柱上表面的roi，考虑到内圆几乎识别不出来，所以在这里内圆采用圆定位的方法获取
    :param img: 初始读取的图像
    :return: 返回roi图像
    """
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.blur(img_gray, (5, 5))  # 降噪滤波
    opening = cv2.morphologyEx(img_blur, cv2.MORPH_OPEN, (7, 7))  # 形态学开运算
    bila = cv2.bilateralFilter(opening, 10, 200, 200)  # 双边滤波消除噪声
    t, dst = cv2.threshold(bila, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # 霍夫变换获取内外圆roi
    circles = cv2.HoughCircles(dst, cv2.HOUGH_GRADIENT, 1, 1000,
                               param1=100, param2=10, minRadius=10, maxRadius=800)
    # cv2.circle(img, (int(circles[0][0][0]), int(circles[0][0][1])), int(circles[0][0][2])-6, (0, 0, 255), 2)
    if circles is not None:  # 如果识别出圆

        mask_new = np.zeros(img.shape, np.uint8)
        for circle in circles[0]:
            #  获取圆的坐标与半径
            x = int(circle[0])
            y = int(circle[1])
            r = int(circle[2])-6
        mask2 = cv2.circle(mask_new, (x, y), r, (255, 255, 255), -1)
        img_roi_out = cv2.bitwise_and(img, mask2)
    return img_roi_out


# 2.阈值分割检测加绘制缺陷
def detect_large_cylinder_result(img, img_roi, thre_value, c_duan, method_duan, yzfg_duan, area_value, blockSize):
    """
    用于多种阈值分割方法检测缺陷
    :param img: 原图，rgb
    :param img_roi: 获取roi区域之后的图
    :param thre_value: 全局阈值分割的阈值或者是局部阈值分割/自适应阈值分割的blocksize
    :param c_duan: 局部阈值分割/自适应阈值分割的常数C
    :param method_duan: 端面检测方法，用于选择图像预处理方法
    :param yzfg_duan: 端面检测方法，用于选择阈值分割方法
    :param area_value: 用于筛选缺陷
    :param blockSize: 当预处理方法为光照补偿时，需要用到此参数
    :return: 返回最终结果
    """
    if method_duan == 'none' or method_duan == '':
        img_roi_gray = cv2.cvtColor(img_roi, cv2.COLOR_BGR2GRAY)
    if method_duan == 'Black_hat':
        img_roi_gray = cv2.cvtColor(img_roi, cv2.COLOR_BGR2GRAY)
        K = np.ones((5, 5), np.uint8)
        img_roi_gray = cv2.morphologyEx(img_roi_gray, cv2.MORPH_BLACKHAT, K)
    if method_duan == 'Fourier_transform':
        img1 = cv2.cvtColor(img_roi, cv2.COLOR_BGR2GRAY)
        f = np.fft.fft2(img1)
        fshift = np.fft.fftshift(f)
        rows, cols = img1.shape
        crow, ccol = int(rows / 2), int(cols / 2)
        fshift[crow - 30:crow + 30, ccol - 30:ccol + 30] = 0  # 设置高通滤波器
        ishift = np.fft.ifftshift(fshift)
        iimg = np.fft.ifft2(ishift)
        iimg = np.abs(iimg)
        iimg = np.array(iimg, dtype='uint8')
        iimg1 = cv2.cvtColor(iimg, cv2.COLOR_GRAY2RGB)  # 傅里叶逆变换
        img_roi_gray = cv2.cvtColor(iimg1, cv2.COLOR_BGR2GRAY)
    if method_duan == 'Light_compensation':
        gray = cv2.cvtColor(img_roi, cv2.COLOR_BGR2GRAY)
        average = np.mean(gray)
        rows_new = int(np.ceil(gray.shape[0] / blockSize))
        cols_new = int(np.ceil(gray.shape[1] / blockSize))
        blockImage = np.zeros((rows_new, cols_new), dtype=np.float32)
        for r in range(rows_new):
            for c in range(cols_new):
                rowmin = r * blockSize
                rowmax = (r + 1) * blockSize
                if (rowmax > gray.shape[0]):
                    rowmax = gray.shape[0]
                colmin = c * blockSize
                colmax = (c + 1) * blockSize
                if (colmax > gray.shape[1]):
                    colmax = gray.shape[1]
                imageROI = gray[rowmin:rowmax, colmin:colmax]
                temaver = np.mean(imageROI)
                blockImage[r, c] = temaver
        blockImage = blockImage - average
        blockImage2 = cv2.resize(blockImage, (gray.shape[1], gray.shape[0]), interpolation=cv2.INTER_CUBIC)
        gray2 = gray.astype(np.float32)
        dst_gzbc = gray2 - blockImage2
        dst_gzbc = dst_gzbc.astype(np.uint8)
        dst_gzbc = cv2.GaussianBlur(dst_gzbc, (3, 3), 0)
        dst_gzbc = cv2.cvtColor(dst_gzbc, cv2.COLOR_GRAY2BGR)
        img_roi_gray = cv2.cvtColor(dst_gzbc, cv2.COLOR_BGR2GRAY)
    if yzfg_duan == 'Global':
        img = cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)), interpolation=cv2.INTER_CUBIC)
        img_roi_gray = cv2.resize(img_roi_gray, (int(img_roi.shape[1] / 2), int(img_roi.shape[0] / 2)),
                             interpolation=cv2.INTER_CUBIC)
        t, dst = cv2.threshold(img_roi_gray, thre_value, 255, cv2.THRESH_BINARY)
        _, contours, _ = cv2.findContours(dst, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        # 阈值分割会把圆也包括进去，所以去掉
        if len(contours) > 2:
            temp = []
            for i in range(len(contours) - 2):
                temp.append(contours[i])
            contours = temp
        else:
            contours = contours
    if yzfg_duan == 'Local':
        img = cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)), interpolation=cv2.INTER_CUBIC)
        img_roi_gray = cv2.resize(img_roi_gray, (int(img_roi.shape[1] / 2), int(img_roi.shape[0] / 2)),
                             interpolation=cv2.INTER_CUBIC)
        dst = cv2.ximgproc.niBlackThreshold(img_roi_gray, 255, cv2.THRESH_BINARY, thre_value, c_duan, cv2.THRESH_BINARY,
                                            cv2.ximgproc.BINARIZATION_NIBLACK)
        _, contours, _ = cv2.findContours(dst, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        # 阈值分割会把圆也包括进去，所以去掉
        if len(contours) > 2:
            temp = []
            for i in range(len(contours) - 2):
                temp.append(contours[i])
            contours = temp
        else:
            contours = contours
    if yzfg_duan == 'Adaptive':
        img = cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)), interpolation=cv2.INTER_CUBIC)
        img_roi_gray = cv2.resize(img_roi_gray, (int(img_roi.shape[1] / 2), int(img_roi.shape[0] / 2)),
                             interpolation=cv2.INTER_CUBIC)
        dst = cv2.adaptiveThreshold(img_roi_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, thre_value, c_duan)
        _, contours, _ = cv2.findContours(dst, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        # 阈值分割会把圆也包括进去，所以去掉
        if len(contours) > 2:
            temp = []
            for i in range(len(contours) - 2):
                temp.append(contours[i])
            contours = temp
        else:
            contours = contours

    # 开始按照面积阈值进行筛选
    cntArea = []
    if contours is not None:
        for i in range(len(contours)):
            area = cv2.contourArea(contours[i])
            if area >= area_value:
                cntArea.append(contours[i])
    if contours is None:
        cntArea = []
    # 根据筛选结果画图
    img_copy = img.copy()
    if len(cntArea) > 0:
        cv2.putText(img_copy, 'NG', (10, 70), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
        cv2.drawContours(img_copy, cntArea, -1, [0, 0, 255], 1)
    else:
        cv2.putText(img_copy, 'OK', (10, 70), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
    cntArea = len(cntArea)
    return img_copy, cntArea


# if __name__ == '__main__':
#     img = cv2.imread("C:/Users/Administrator/MVS/Data/camera0 (00F38166000)/Image_106.jpg")
#     img = cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)),
#                       interpolation=cv2.INTER_CUBIC)
#     img_roi = get_roi_large_cylinder(img)
#     # # result, counts = detect_large_cylinder_result(img, img_roi, 100, 3, 'Global', 0)
#     result, counts = detect_large_cylinder_result(img, img_roi, 409, 8.3, 'Black_hat', 'Local', 0.83, 16)
#     # # result, counts = detect_large_cylinder_result(img, img_roi, 11, 13, 'Adaptive', 0)
#     cv2.imshow('img_roi', img_roi)
#     cv2.imshow('result', result)
#     cv2.waitKey()
#     cv2.destroyAllWindows()