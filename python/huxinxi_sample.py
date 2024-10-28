# coding=utf-8
import numpy as np
#//计算两个一维数组的互信息
def mutual_information(X, Y):
    p_xy = np.zeros((len(set(X)), len(set(Y))))
    p_x = np.zeros(len(set(X)))
    p_y = np.zeros(len(set(Y)))
    for i in range(len(X)):
        x = X[i]
        y = Y[i]
        p_xy[x][y] += 1
        p_x[x] += 1
        p_y[y] += 1
    p_xy /= len(X)
    p_x /= len(X)
    p_y /= len(Y)
    mi = 0
    for i in range(len(set(X))):
        for j in range(len(set(Y))):
            if p_xy[i][j] > 0:
                mi += p_xy[i][j] * np.log2(p_xy[i][j] / (p_x[i] * p_y[j]))
    return mi

X = np.random.randint(0, 10, 20)
Y = np.random.randint(0, 10, 20)
print(X)
print(X)
mi = mutual_information(X, Y)
print(mi)

