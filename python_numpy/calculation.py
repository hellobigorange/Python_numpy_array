import numpy as np


a = np.array([1, 2, 3, 4])
b = np.ones(4)

"""
//**********************
数组点运算
**********************//
"""
print('点运算加减乘除幂', a+b, a-b, a*b, a/b, a**2)
print('对每个元素三角运算', np.sin(a), np.cos(a), np.tan(a))
print('对每个元素log运算(10为底，e为底)', np.log10(a), np.log(a))
print('对每个元素exp运算 )', np.exp(a))
print('判断每个元素是否大于一个定值', a > 2)

"""
//**********************
数组（矩阵）运算，我觉得最好转成mat运算
**********************//
"""
print('乘法', np.mat(a).T.dot(np.mat(b)), np.dot(np.mat(a).T, np.mat(b)))
print('转置', np.mat(a).T)
print('矩阵分区，矩阵元素小于2为2，大于3为3', np.clip(np.mat(a), 2, 3))

"""
//**********************
数组求和，最大，最小，列/行最大最小...
**********************//
"""
print('数组和,最大，最小', np.sum(a), np.max(a), np.min(a))
c = a.reshape(2, 2)
print('每一列求和', np.sum(c, axis=0))
print('每一行求和', np.sum(c, axis=1))
print('最大值索引', np.argmax(a))
print('平均值，中位数', np.mean(a), np.median(a))
print('累加', np.cumsum(a))
print('累差', np.diff(a))
print('返回非0元素下标', np.nonzero(np.mat(a)))
print('逐行排序', np.sort(np.array([[3, 2], [1, 3]])))

