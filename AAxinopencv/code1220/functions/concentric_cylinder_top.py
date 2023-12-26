import cv2
import numpy as np
# from skimage.morphology import remove_small_objects


# 外圆roi获取
def get_roi_concentric(img):
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
    print(1111111111111111111111)
    # 霍夫变换获取内外圆roi
    circles = cv2.HoughCircles(dst, cv2.HOUGH_GRADIENT, 1, 1000,
                               param1=100, param2=10, minRadius=10, maxRadius=800)
    # cv2.circle(img, (int(circles[0][0][0]), int(circles[0][0][1])), int(circles[0][0][2]), (0, 0, 255), 2)
    if circles is not None:  # 如果识别出圆
        print(2222222222222222222222222)
        mask = np.zeros(img.shape, np.uint8)
        mask_new = np.zeros(img.shape, np.uint8)
        for circle in circles[0]:
            #  获取圆的坐标与半径
            x = int(circle[0])
            y = int(circle[1])
            r = int(circle[2])
        print(r)
        if 190 <= r <= 210:
            mask2 = cv2.circle(mask_new, (x, y), r + 50, (255, 255, 255), -1)
            print(3333333333333333333333333333)
            img_roi_in = cv2.bitwise_and(img, mask2)
            cv2.circle(img_roi_in, (x, y), r + 10, (0, 0, 0), -1)
            mask1 = cv2.circle(mask, (x, y), r - 55, (255, 255, 255), -1)
            # mask1 = cv2.circle(img_roi_in, (x, y), r - 15, (0, 0, 0), -1)
            img_roi_out = cv2.bitwise_and(img, mask1)
            print(r)
            return img_roi_out, img_roi_in
        if 245 <= r <= 265:
            print(4444444444444444444444444444444)
            mask2 = cv2.circle(mask_new, (x, y), r - 10, (255, 255, 255), -1)
            img_roi_in = cv2.bitwise_and(img, mask2)
            cv2.circle(img_roi_in, (x, y), r - 50, (0, 0, 0), -1)
            mask1 = cv2.circle(mask, (x, y), r - 110, (255, 255, 255), -1)
            # mask1 = cv2.circle(img_roi_in, (x, y), r - 15, (0, 0, 0), -1)
            img_roi_out = cv2.bitwise_and(img, mask1)
            print(r)
            return img_roi_out, img_roi_in
        if r < 190:
            img_roi_out, img_roi_in = [], []
            return img_roi_out, img_roi_in
    else:
        img_roi_out, img_roi_in = [], []
        return img_roi_out, img_roi_in


# 检测函数
def detect_concentric_result(img, img_big_loop, img_small_loop, thre_value, c_duan, method_duan, yzfg_duan, area_value, blockSize):
    """
    此函数用于检测缺陷，采用阈值分割的方式
    :param img: 最初读取的原图
    :param img_big_loop: 获取的roi中的大圆环
    :param img_small_loop: 获取的roi中的小圆环
    :param thre_value: 阈值分割的阈值
    :param min_value: 移除缺陷的最小值，适用于remove_small_objects函数
    :param len_value: 根据长度需求，过滤掉小于该长度值的缺陷
    :param area_value: 根据面积需求，过滤掉小于该面积值的缺陷
    :return: 返回检测后的图片
    """
    img_copy = img.copy()
    # 首先判断roi是否在真的获取成功
    if img_big_loop == [] or img_small_loop == []:    # 未获取到roi
        cv2.putText(img_copy, 'OK', (10, 30), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
        print(22222)
    else:
        if method_duan == 'none' or method_duan == '':
            gray_big_loop = cv2.cvtColor(img_big_loop, cv2.COLOR_BGR2GRAY)
            gray_small_loop = cv2.cvtColor(img_small_loop, cv2.COLOR_BGR2GRAY)
            gray_blur_small_loop = cv2.blur(gray_small_loop, (3, 3))
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
            gray_blur_small_loop = cv2.blur(gray_small_loop, (3, 3))
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
            gray_blur_small_loop = cv2.blur(gray_small_loop, (3, 3))
        if yzfg_duan == 'Global':
            t1, dst_big = cv2.threshold(gray_big_loop, thre_value, 255, cv2.THRESH_BINARY)
            dst_big1 = dst_big > 0.08
            # dst_big_result = remove_small_objects(dst_big1, min_size=1, connectivity=1)
            dst_big_result = np.array(dst_big1, dtype='uint8')
            _, contours_big_loop, _ = cv2.findContours(dst_big_result, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
            t2, dst_small = cv2.threshold(gray_blur_small_loop, thre_value, 255, cv2.THRESH_BINARY)
            dst_small1 = dst_small > 0.08
            # dst_small_result = remove_small_objects(dst_small1, min_size=1, connectivity=1)
            dst_small_result = np.array(dst_small, dtype='uint8')
            _, contours_small_loop, _ = cv2.findContours(dst_small_result, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        if yzfg_duan == 'Local':
            dst_big = cv2.ximgproc.niBlackThreshold(gray_big_loop, 255, cv2.THRESH_BINARY, thre_value, c_duan,
                                                    cv2.THRESH_BINARY, cv2.ximgproc.BINARIZATION_NIBLACK)
            dst_big1 = dst_big > 0.08
            # dst_big_result = remove_small_objects(dst_big1, min_size=1, connectivity=1)
            dst_big_result = np.array(dst_big1, dtype='uint8')
            _, contours_big_loop, _ = cv2.findContours(dst_big_result, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
            dst_small = cv2.ximgproc.niBlackThreshold(gray_blur_small_loop, 255, cv2.THRESH_BINARY, thre_value, c_duan,
                                                    cv2.THRESH_BINARY, cv2.ximgproc.BINARIZATION_NIBLACK)
            dst_small1 = dst_small > 0.08
            # dst_small_result = remove_small_objects(dst_small1, min_size=1, connectivity=1)
            dst_small_result = np.array(dst_small1, dtype='uint8')
            _, contours_small_loop, _ = cv2.findContours(dst_small_result, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        if yzfg_duan == 'Adaptive':
            dst_big = cv2.adaptiveThreshold(gray_big_loop, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,
                                            thre_value, c_duan)
            dst_big1 = dst_big > 0.08
            # dst_big_result = remove_small_objects(dst_big1, min_size=1, connectivity=1)
            dst_big_result = np.array(dst_big1, dtype='uint8')
            _, contours_big_loop, _ = cv2.findContours(dst_big_result, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
            dst_small = cv2.adaptiveThreshold(gray_blur_small_loop, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,
                                            thre_value, c_duan)
            dst_small1 = dst_small > 0.08
            # dst_small_result = remove_small_objects(dst_small1, min_size=1, connectivity=1)
            dst_small_result = np.array(dst_small1, dtype='uint8')
            _, contours_small_loop, _ = cv2.findContours(dst_small_result, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        # 开始按照面积阈值筛选缺陷
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
            if len(cntArea_small) > 1:
                cv2.drawContours(img_copy, cntArea_small, -1, [0, 0, 255], 1)
            print(1)
        if len(cntArea_big) != 0 and len(cntArea_small) == 0:
            cv2.putText(img_copy, 'NG', (10, 70), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 2)
            cv2.drawContours(img_copy, cntArea_big, -1, [0, 0, 255], 1)
            print(2)
        if len(cntArea_big) == 0 and len(cntArea_small) != 0:
            if len(cntArea_small) > 1:
                cv2.putText(img_copy, 'NG', (10, 70), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 2)
                cv2.drawContours(img_copy, cntArea_small, -1, [0, 0, 255], 1)
            else:
                cv2.putText(img_copy, 'OK', (10, 70), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
            print(3)
        if len(cntArea_big) == 0 and len(cntArea_small) == 0:
            cv2.putText(img_copy, 'OK', (10, 70), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
        cntArea = len(cntArea_big) + len(cntArea_small)
        return img_copy, cntArea


if __name__ == '__main__':
    img = cv2.imread("C:/Users/Administrator/Desktop/1217/1217/pic/pictures_concentric/MV-CA060-15GM (00E81333353)/3056.jpg")
    print(img.shape)
    # img = cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)), interpolation=cv2.INTER_CUBIC)
    dst1, dst2 = get_roi_concentric(img)
    result_big, _ = detect_concentric_result(img, dst1, dst2, 83, 2, 'none', 'Local', 0, 16)
    cv2.imshow('1', dst1)
    cv2.imshow('2', dst2)

    cv2.imshow('3', img)
    cv2.imwrite('../test.jpg', result_big)
    cv2.waitKey()
    cv2.destroyAllWindows()


