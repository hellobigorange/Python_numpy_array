# coding:utf-8
import pandas as pd
import numpy as np


"""
//**********************
七、pandas导入导出数据
**********************//
"""
data1 = pd.read_excel('data/apple.xlsx')
print(data1)

data2 = pd.read_csv('data/ex1data1.csv')
print(data2)
data = pd.read_csv('data/ex1data2.txt')
print(data)
# print('读取csv文件', data)

"""
//**********************
八、pandas修改数据后保存
**********************//
"""
data1['ball'] = np.arange(data1.shape[0])
# 保存为pickle文件
data1.to_pickle('data/apple.pickle')
data2.to_csv('data/orange.csv')
data3 = pd.read_pickle('data/apple.pickle')
print(data3)