import numpy as np

"""
//**********************
数组合并与分割
**********************//
"""

a = np.mat(np.ones(3))
b = np.mat(2*np.ones(3))
c = np.arange(12).reshape(3, 4)
# 合并
print('上下合并', np.vstack((a, b)), np.concatenate((a, b), axis=0))
print('左右合并', np.hstack((a, b)), np.concatenate((a, b), axis=1))

# 分割
print('左右分割,将(3,4)分成两个(3,2)', np.split(c, 2, axis=1), np.hsplit(c, 2))
print('上下分割,将(3,4)分成三个(1,4)', np.split(c, 3, axis=0), np.vsplit(c, 3))
print('对3行进行不均等分割', np.array_split(c, 2, axis=0))