import cv2
import numpy as np


# 原图转二值图
def trans2binary(img):
    """
    此函数是为了定位圆而做的前期准备
    :param img: 原图像
    :return: 返回二值图
    """
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # img_blur = cv2.blur(img_gray, (5, 5))  # 降噪滤波
    # opening = cv2.morphologyEx(img_blur, cv2.MORPH_OPEN, (7, 7))  # 形态学开运算
    # bila = cv2.bilateralFilter(opening, 10, 200, 200)  # 双边滤波消除噪声
    t, dst = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # _, contours, _ = cv2.findContours(dst, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    # cv2.drawContours(img, contours, -1, [0, 0, 255], 1)
    # cv2.imshow('result', dst)
    # cv2.waitKey()
    # cv2.destroyAllWindows()
    return dst


# 圆定位
def circle_position(img_binary):
    """
    此函数利用霍夫圆变换检测圆心位置和半径
    :param img_binary: 二值化的图片
    :return: 返回圆的圆心和半径
    """
    circles = cv2.HoughCircles(img_binary, cv2.HOUGH_GRADIENT, 1, 1000,
                               param1=100, param2=10, minRadius=10, maxRadius=800)
    if circles is not None:  # 如果识别出圆
        for circle in circles[0]:
            #  获取圆的坐标与半径
            x = int(circle[0])
            y = int(circle[1])
            r = int(circle[2])
    else:
        # 如果识别不出，显示圆心不存在
        x, y, r = None, None, None
    return x, y, r


# 获取roi
def get_roi_lid(img, dst, template):
    """
    此函数作用是获取端面检测区域
    :param img: img是初始读取的原图
    :param x: 圆定位获取的圆心横坐标
    :param y: 圆定位获取的圆心纵坐标
    :param r: 圆定位获取的圆的半径
    :return: 返回roi区域的掩膜图像
    """
    mask_big = np.zeros(img.shape, np.uint8)
    mask_small = np.zeros(img.shape, np.uint8)
    _, contours, _ = cv2.findContours(dst, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    print(len(contours))
    if len(contours) == 4:  # 判断是否是4个圆圈
        temp = []
        for i in range(len(contours)):
            temp.append(len(contours[i]))
        theset = frozenset(temp)
        theset = sorted(theset, reverse=True)
        first_contours = contours[temp.index(theset[0])]
        second_contours = contours[temp.index(theset[1])]
        third_contours = contours[temp.index(theset[2])]
        fourth_contours = contours[temp.index(theset[3])]
        big_loop_contours = [first_contours, second_contours]
        small_loop_contours = [third_contours, fourth_contours]
        mask_big_loop = cv2.drawContours(mask_big, big_loop_contours, -1, [255, 255, 255], -1)
        mask_small_loop = cv2.drawContours(mask_small, small_loop_contours, -1, [255, 255, 255], -1)
        img_big_loop = cv2.bitwise_and(img, mask_big_loop)
        img_small_loop = cv2.bitwise_and(img, mask_small_loop)
    else:
        # 由于直接用四个圆的轮廓来定位鲁棒性不高，所以这里用模板匹配定位内圆的位置,然后依次获取外层的各个圆
        target = img
        tem_h, tem_w = template.shape[0:2]
        result = cv2.matchTemplate(target, template, cv2.TM_SQDIFF_NORMED)  # 执行模板匹配
        cv2.normalize(result, result, 0, 1, cv2.NORM_MINMAX, -1)  # 对结果进行归一化处理
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)  # 根据一维矩阵的最大值和最小值来匹配，并确定其位置
        mask = np.zeros(target.shape, np.uint8)
        cv2.rectangle(mask, min_loc, (min_loc[0] + tem_w, min_loc[1] + tem_h), (255, 255, 255), -1)
        img_result = cv2.bitwise_and(target, mask)
        img_temp = img_result[min_loc[1]:min_loc[1] + tem_h, min_loc[0]:min_loc[0] + tem_w]
        x, y = min_loc[0] + tem_w / 2, min_loc[1] + tem_h / 2
        mask_small_loop = cv2.circle(mask_small, (int(x), int(y)), 76, (255, 255, 255), -1)
        mask_small_loop = cv2.circle(mask_small_loop, (int(x), int(y)), 70, (0, 0, 0), -1)
        img_small_loop = cv2.bitwise_and(img, mask_small_loop)
        mask_big_loop = cv2.drawContours(mask_big, [contours[-1]], -1, (255, 255, 255), -1)
        mask_big_loop = cv2.circle(mask_big_loop, (int(x), int(y)), 85, (0, 0, 0), -1)
        img_big_loop = cv2.bitwise_and(img, mask_big_loop)
        # circles = cv2.HoughCircles(dst, cv2.HOUGH_GRADIENT, 1, 1000,
        #                            param1=100, param2=10, minRadius=10, maxRadius=800)
        # cv2.circle(img, (int(x), int(y)), 70, (0, 0, 255), 1)
        # cv2.circle(img, (int(x), int(y)), 76, (0, 0, 255), 1)
        # cv2.circle(img, (int(x), int(y)), 85, (0, 0, 255), 1)
        # cv2.circle(img, (int(x), int(y)), 120, (0, 0, 255), 1)
    return img_big_loop, img_small_loop


# 检测函数
def detect_lid_result(img, img_big_loop, img_small_loop, thre_value, c_duan, method_duan, yzfg_duan, area_value, blockSize):
    """
    :param img: 原图rgb
    :param img_big_loop: 大圆环图片
    :param img_small_loop: 小圆环图片
    :param thre_value: 全局阈值分割的阈值/局部阈值分割或自适应阈值分割的block
    :param c_duan: 局部阈值分割或自适应阈值分割的常数c
    :param method_duan: 端面预处理方法
    :param yzfg_duan: 端面阈值分割方法
    :param area_value: 用于筛选缺陷的面积阈值
    :param blockSize: 预处理是光照补偿时的blockSize
    :return: 最终结果图和轮廓信息
    """
    img_copy = img.copy()
    if method_duan == 'none' or method_duan == '':
        gray_big_loop = cv2.cvtColor(img_big_loop, cv2.COLOR_BGR2GRAY)
        gray_small_loop = cv2.cvtColor(img_small_loop, cv2.COLOR_BGR2GRAY)
    if method_duan == 'Black_hat':
        gray_big_loop = cv2.cvtColor(img_big_loop, cv2.COLOR_BGR2GRAY)
        gray_small_loop = cv2.cvtColor(img_small_loop, cv2.COLOR_BGR2GRAY)
        K = np.ones((5, 5), np.uint8)
        gray_big_loop = cv2.morphologyEx(gray_big_loop, cv2.MORPH_BLACKHAT, K)
        gray_small_loop = cv2.morphologyEx(gray_small_loop, cv2.MORPH_BLACKHAT, K)
    if method_duan == 'Fourier_transform':
        img1 = cv2.cvtColor(img_big_loop, cv2.COLOR_BGR2GRAY)
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
        gray_big_loop = cv2.cvtColor(iimg1, cv2.COLOR_BGR2GRAY)
        img2 = cv2.cvtColor(img_small_loop, cv2.COLOR_BGR2GRAY)
        f = np.fft.fft2(img2)
        fshift = np.fft.fftshift(f)
        rows, cols = img2.shape
        crow, ccol = int(rows / 2), int(cols / 2)
        fshift[crow - 30:crow + 30, ccol - 30:ccol + 30] = 0  # 设置高通滤波器
        ishift = np.fft.ifftshift(fshift)
        iimg3 = np.fft.ifft2(ishift)
        iimg3 = np.abs(iimg3)
        iimg3 = np.array(iimg3, dtype='uint8')
        iimg3 = cv2.cvtColor(iimg3, cv2.COLOR_GRAY2RGB)  # 傅里叶逆变换
        gray_small_loop = cv2.cvtColor(iimg3, cv2.COLOR_BGR2GRAY)
    if method_duan == 'Light_compensation':
        gray1 = cv2.cvtColor(img_big_loop, cv2.COLOR_BGR2GRAY)
        average = np.mean(gray1)
        rows_new = int(np.ceil(gray1.shape[0] / blockSize))
        cols_new = int(np.ceil(gray1.shape[1] / blockSize))
        blockImage = np.zeros((rows_new, cols_new), dtype=np.float32)
        for r in range(rows_new):
            for c in range(cols_new):
                rowmin = r * blockSize
                rowmax = (r + 1) * blockSize
                if (rowmax > gray1.shape[0]):
                    rowmax = gray1.shape[0]
                colmin = c * blockSize
                colmax = (c + 1) * blockSize
                if (colmax > gray1.shape[1]):
                    colmax = gray1.shape[1]
                imageROI = gray1[rowmin:rowmax, colmin:colmax]
                temaver = np.mean(imageROI)
                blockImage[r, c] = temaver
        blockImage = blockImage - average
        blockImage2 = cv2.resize(blockImage, (gray1.shape[1], gray1.shape[0]), interpolation=cv2.INTER_CUBIC)
        gray2 = gray1.astype(np.float32)
        dst_gzbc = gray2 - blockImage2
        dst_gzbc = dst_gzbc.astype(np.uint8)
        dst_gzbc = cv2.GaussianBlur(dst_gzbc, (3, 3), 0)
        dst_gzbc = cv2.cvtColor(dst_gzbc, cv2.COLOR_GRAY2BGR)
        gray_big_loop = cv2.cvtColor(dst_gzbc, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(img_small_loop, cv2.COLOR_BGR2GRAY)
        average = np.mean(gray2)
        rows_new = int(np.ceil(gray2.shape[0] / blockSize))
        cols_new = int(np.ceil(gray2.shape[1] / blockSize))
        blockImage = np.zeros((rows_new, cols_new), dtype=np.float32)
        for r in range(rows_new):
            for c in range(cols_new):
                rowmin = r * blockSize
                rowmax = (r + 1) * blockSize
                if (rowmax > gray2.shape[0]):
                    rowmax = gray2.shape[0]
                colmin = c * blockSize
                colmax = (c + 1) * blockSize
                if (colmax > gray2.shape[1]):
                    colmax = gray2.shape[1]
                imageROI = gray2[rowmin:rowmax, colmin:colmax]
                temaver = np.mean(imageROI)
                blockImage[r, c] = temaver
        blockImage = blockImage - average
        blockImage2 = cv2.resize(blockImage, (gray2.shape[1], gray2.shape[0]), interpolation=cv2.INTER_CUBIC)
        gray2 = gray2.astype(np.float32)
        dst_gzbc = gray2 - blockImage2
        dst_gzbc = dst_gzbc.astype(np.uint8)
        dst_gzbc = cv2.GaussianBlur(dst_gzbc, (3, 3), 0)
        dst_gzbc = cv2.cvtColor(dst_gzbc, cv2.COLOR_GRAY2BGR)
        gray_small_loop = cv2.cvtColor(dst_gzbc, cv2.COLOR_BGR2GRAY)
    if yzfg_duan == 'Global':
        t, dst_big = cv2.threshold(gray_big_loop, thre_value, 255, cv2.THRESH_BINARY)
        t, dst_small = cv2.threshold(gray_small_loop, thre_value, 255, cv2.THRESH_BINARY)
        _, contours_big_loop, _ = cv2.findContours(dst_big, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        _, contours_small_loop, _ = cv2.findContours(dst_small, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        contours_big_loop = sorted(contours_big_loop, key=len)
        contours_small_loop = sorted(contours_small_loop, key=len)
    if yzfg_duan == 'Local':
        dst_big = cv2.ximgproc.niBlackThreshold(gray_big_loop, 255, cv2.THRESH_BINARY, thre_value, c_duan, cv2.THRESH_BINARY,
                                            cv2.ximgproc.BINARIZATION_NIBLACK)
        dst_small = cv2.ximgproc.niBlackThreshold(gray_small_loop, 255, cv2.THRESH_BINARY, thre_value, c_duan,
                                            cv2.THRESH_BINARY, cv2.ximgproc.BINARIZATION_NIBLACK)
        _, contours_big_loop, _ = cv2.findContours(dst_big, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        _, contours_small_loop, _ = cv2.findContours(dst_small, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        contours_big_loop = sorted(contours_big_loop, key=len)
        contours_small_loop = sorted(contours_small_loop, key=len)
    if yzfg_duan == 'Adaptive':
        dst_big = cv2.adaptiveThreshold(gray_big_loop, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,
                                    thre_value, c_duan)
        dst_small = cv2.adaptiveThreshold(gray_small_loop, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,
                                    thre_value, c_duan)
        _, contours_big_loop, _ = cv2.findContours(dst_big, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        _, contours_small_loop, _ = cv2.findContours(dst_small, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        contours_big_loop = sorted(contours_big_loop, key=len)
        contours_small_loop = sorted(contours_small_loop, key=len)
    if len(contours_big_loop) >= 2:
        temp = []
        for i in range(len(contours_big_loop) - 2):
            temp.append(contours_big_loop[i])
        contours_big_loop = temp
    else:
        contours_big_loop = []
    if len(contours_small_loop) >= 2:
        temp1 = []
        for i in range(len(contours_small_loop) - 2):
            temp1.append(contours_small_loop[i])
        contours_small_loop = temp1
    else:
        contours_small_loop = []
    print(len(contours_big_loop))
    print(len(contours_small_loop))

    # 按照面积筛选阈值
    cntArea_big = []
    cntArea_small = []
    if len(contours_big_loop) != 0 and len(contours_small_loop) != 0:
        for i in range(len(contours_big_loop)):
            area_big = cv2.contourArea(contours_big_loop[i])
            if area_big >= area_value:
                cntArea_big.append(contours_big_loop[i])
        for j in range(len(contours_small_loop)):
            area_small = cv2.contourArea(contours_small_loop[j])
            if area_small >= area_value:
                cntArea_small.append(contours_small_loop[j])
    if len(contours_big_loop) != 0 and len(contours_small_loop) == 0:
        for i in range(len(contours_big_loop)):
            area_big = cv2.contourArea(contours_big_loop[i])
            if area_big >= area_value:
                cntArea_big.append(contours_big_loop[i])
    if len(contours_big_loop) == 0 and len(contours_small_loop) != 0:
        for j in range(len(contours_small_loop)):
            area_small = cv2.contourArea(contours_small_loop[j])
            if area_small >= area_value:
                cntArea_small.append(contours_small_loop[j])
    if len(contours_big_loop) == 0 and len(contours_small_loop) == 0:
        cntArea_big = []
        cntArea_small = []

    # 根据筛选结果画图
    if len(cntArea_big) != 0 and len(cntArea_small) != 0:
        cv2.putText(img_copy, 'NG', (10, 70), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 2)
        cv2.drawContours(img_copy, cntArea_big, -1, [0, 0, 255], 1)
        cv2.drawContours(img_copy, cntArea_small, -1, [0, 0, 255], 1)
        print(1)
    if len(cntArea_big) != 0 and len(cntArea_small) == 0:
        cv2.putText(img_copy, 'NG', (10, 70), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 2)
        cv2.drawContours(img_copy, cntArea_big, -1, [0, 0, 255], 1)
        print(2)
    if len(cntArea_big) == 0 and len(cntArea_small) != 0:
        cv2.putText(img_copy, 'NG', (10, 70), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 2)
        cv2.drawContours(img_copy, cntArea_small, -1, [0, 0, 255], 1)
        print(3)
    if len(cntArea_big) == 0 and len(cntArea_small) == 0:
        cv2.putText(img_copy, 'OK', (10, 70), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
        print(4)
    cntArea = len(cntArea_big) + len(cntArea_small)
    return img_copy, cntArea


# # start = time.time()
# img = cv2.imread('../0731/1223.bmp')
# temp = cv2.imread('../0731/11234_temp.jpg')
# img = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)), interpolation=cv2.INTER_CUBIC)
# temp = cv2.resize(temp, (int(temp.shape[1]/2), int(temp.shape[0]/2)), interpolation=cv2.INTER_CUBIC)
# dst = trans2binary(img)
# mask_big_loop, mask_small_loop = get_roi_lid(img, dst, temp)
# dst1 = detect_lid_result(img, mask_big_loop, mask_small_loop, 181, 0, 'none', 'Local', 0, 16)
# print('检测耗时：', time.time()-start)
# # print(m)
# # print(circle)
#
# cv2.imshow('1', dst1)
# # cv2.imshow('2', dst2)
# # cv2.imshow('3', mask_small_loop)
# # cv2.imshow('4', mask_big_loop)
# # cv2.imwrite('3.jpg', dst)
# # cv2.imwrite('test.jpg', img_circle1)
#
# # cv2.imshow('result', result)
# # cv2.imwrite('test.jpg', result)
# # cv2.imshow('origin', img)
# cv2.waitKey()
# cv2.destroyAllWindows()