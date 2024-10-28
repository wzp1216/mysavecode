#!/usr/bin/env python
# coding=utf-8
import math

# 定义一个计算熵的函数
def entropy(data):
    counts = {}
    for d in data:
        if d not in counts:
            counts[d] = 0
        counts[d] += 1

    total = len(data)
    entropy = 0.0
    for count in counts.values():
        prob = float(count) / total
        entropy -= prob * math.log(prob, 2)

    return entropy

# 用例子数据计算熵值
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print("数据集: ", data)
print("熵值: ", entropy(data))

