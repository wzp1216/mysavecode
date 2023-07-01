import cv2
from glob import glob
import numpy as np


# 模板匹配
def get_roi(target, template):
    """根据模板匹配来获取图像的roi区域：
    模板图片需要自己裁剪，搭建好平台之后拍摄一张图片裁剪合适的大小即可
    ***********************************************************************************
    对于cv2.TM_SQDIFF及cv2.TM_SQDIFF_NORMED方法min_val越趋近与0匹配度越好，匹配位置取min_loc
    对于其他方法max_val越趋近于1匹配度越好，匹配位置取max_loc
    :param target: 需要进行模板匹配获取roi的图像
    :param template: 模板图片（需要自己裁剪输入到函数）
    :return:模板匹配后的图像，只有模板区域，别的地方都是黑色
    """
    tem_h, tem_w = template.shape[0:2]
    result = cv2.matchTemplate(target, template, cv2.TM_SQDIFF_NORMED)  # 执行模板匹配
    cv2.normalize(result, result, 0, 1, cv2.NORM_MINMAX, -1)  # 对结果进行归一化处理
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)  # 根据一维矩阵的最大值和最小值来匹配，并确定其位置
    strmin_val = str(min_val)  # 匹配值转化为字符串
    # cv2.rectangle(target, min_loc, (min_loc[0] + tem_w, min_loc[1] + tem_h), (0, 0, 225), 2)    # 可视化匹配结果
    mask = np.zeros(target.shape, np.uint8)
    cv2.rectangle(mask, min_loc, (min_loc[0] + tem_w, min_loc[1] + tem_h), (255, 255, 255), -1)
    img_result = cv2.bitwise_and(target, mask)
    img_temp = img_result[min_loc[1]:min_loc[1] + tem_h, min_loc[0]:min_loc[0] + tem_w]
    return img_result, img_temp, min_loc, tem_w, tem_h


# 检测函数
def detect_concentric_side(img, img_roi, img_temp, min_loc, temp_w, temp_h, method_side, yzfg_side, thre_value, c_ce,
                           area_value, blockSize):
    """
    :param img_roi: 经过roi处理之后的图像
    :param img_temp: 模板匹配后的图像（无位置信息）
    :param min_loc: 模板匹配后的图像的左上角在原图像的位置信息
    :param temp_w: 模板图像的宽
    :param temp_h: 模板图像的高
    :param thre_value: 全局阈值分割的阈值或者是局部阈值分割/自适应阈值分割的blocksize
    :param c_ce: 局部阈值分割/自适应阈值分割的常量c
    :param blockSize: 当预处理方法为光照补偿时选用的blockSize
    :return: 返回缺陷的轮廓信息
    """
    if method_side == 'none' or method_side == '':
        img_roi_gray = cv2.cvtColor(img_roi, cv2.COLOR_BGR2GRAY)
    if method_side == 'Black_hat':
        dst_gray = cv2.cvtColor(img_roi, cv2.COLOR_BGR2GRAY)
        K = np.ones((9, 9), np.uint8)
        img_black = cv2.morphologyEx(dst_gray, cv2.MORPH_BLACKHAT, K)
        img_roi_gray = img_black
    if method_side == 'Fourier_transform':
        img1 = cv2.cvtColor(img_temp, cv2.COLOR_BGR2GRAY)
        print(img_temp.shape)
        print(img1.shape)
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
        # 接下来将经过傅里叶变换之后的图像定位到原始图像中
        mask = np.zeros(img_roi.shape, np.uint8)
        # mask[min_loc[1]:min_loc[1] + temp_h, min_loc[0]:min_loc[0] + temp_w] = iimg1
        # 因为傅里叶变换图片的顶部和底部会存在白边，因此这里对图片进行切片操作
        # iimg2 = iimg1[50:iimg1.shape[0] - 50, 50:iimg1.shape[1] - 50]
        # mask[min_loc[1] + 50:min_loc[1] + iimg1.shape[0] - 50, min_loc[0] + 50:min_loc[0] + temp_w - 50] = iimg2
        img_roi_gray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    if method_side == 'Light_compensation':
        gray = cv2.cvtColor(img_temp, cv2.COLOR_BGR2GRAY)
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
        mask = np.zeros(img_roi.shape, np.uint8)
        print(mask.shape)
        # mask[min_loc[1]:min_loc[1] + temp_h, min_loc[0]:min_loc[0] + temp_w] = iimg1
        # 因为光照补偿之后的图片顶部和底部会存在白边，因此这里对图片进行切片操作
        iimg1 = dst_gzbc
        print(iimg1.shape)
        iimg2 = iimg1[5:iimg1.shape[0] - 5, 10:iimg1.shape[1] - 10]
        mask[min_loc[1] + 5:min_loc[1] + iimg1.shape[0] - 5, min_loc[0] + 10:min_loc[0] + temp_w - 10] = iimg2
        img_roi_gray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    if yzfg_side == 'Global':
        img_roi_gray = cv2.resize(img_roi_gray, (int(img_roi.shape[1] / 2), int(img_roi.shape[0] / 2)),
                             interpolation=cv2.INTER_CUBIC)
        t, dst = cv2.threshold(img_roi_gray, thre_value, 255, cv2.THRESH_BINARY)
        _, contours, _ = cv2.findContours(dst, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    if yzfg_side == 'Local':
        img_roi_gray = cv2.resize(img_roi_gray, (int(img_roi.shape[1] / 2), int(img_roi.shape[0] / 2)),
                                  interpolation=cv2.INTER_CUBIC)
        dst = cv2.ximgproc.niBlackThreshold(img_roi_gray, 255, cv2.THRESH_BINARY, thre_value, c_ce, cv2.THRESH_BINARY,
                                            cv2.ximgproc.BINARIZATION_NIBLACK)
        _, contours, _ = cv2.findContours(dst, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        print(len(contours))
    if yzfg_side == 'Adaptive':
        img_roi_gray = cv2.resize(img_roi_gray, (int(img_roi.shape[1] / 2), int(img_roi.shape[0] / 2)),
                                  interpolation=cv2.INTER_CUBIC)
        dst = cv2.adaptiveThreshold(img_roi_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,
                                    thre_value, c_ce)
        _, contours, _ = cv2.findContours(dst, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

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
    img_copy = cv2.resize(img_copy, (int(img_copy.shape[1] / 2), int(img_copy.shape[0] / 2)), interpolation=cv2.INTER_CUBIC)
    if len(cntArea) > 0:
        cv2.putText(img_copy, 'NG', (10, 70), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 2)
        cv2.drawContours(img_copy, cntArea, -1, [0, 0, 255], 1)
    else:
        cv2.putText(img_copy, 'OK', (10, 70), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
    return img_copy, cntArea


if __name__ == '__main__':
    file5 = glob("C:/Users/Administrator/MVS/Data/camera0 (00F38166000)" + '/*jpg')[0]
    img = cv2.imread(file5)
    temp = cv2.imread("C:/Users/Administrator/Desktop/mb/Image_18.jpg")
    img_roi, img_temp, min_loc, temp_w, temp_h = get_roi(img, temp)
    result, contours = detect_concentric_side(img, img_roi, img_temp, min_loc, temp_w, temp_h, 'Black_hat', 'Local', 113, 3.1, 1.8, 16)
    # result_pic = get_concentric_result(img, contours, 0)
    # cv2.imwrite('../iimg.jpg', mask)

    # cv2.imshow('result', result)
    # cv2.imshow('result1', contours)
    cv2.imwrite('./paraments/result_kg.jpg', result)
    # cv2.waitKey()
    # cv2.destroyAllWindows()