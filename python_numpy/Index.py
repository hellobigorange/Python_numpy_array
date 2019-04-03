import numpy as np

"""
//**********************
根据位置索引元素的值
**********************//
"""
a = np.arange(3, 15)
print('a向量的第三个元素6', a[3])
b = a.reshape(3, 4)
print('b的第二行[11,12,13,14]', b[2], b[2, :])
print('b的第二列[5,9,13]', b[:, 2])
print('b的b[0][3] 6', b[0][3], b[0, 3])
print('切片索引b的第1行，第1.2列 [8,9]', b[1, 1:3])


"""
//**********************
迭代每一行，每一列，没一个元素值
**********************//
"""

for row in b:
    print('行', row)

for column in b.T:
    print('列', column)

for item in b.flat:
    print('项', item)