import numpy as np

list1 = [[1, 2, 3], [4, 5, 6]]

# 列表转为numpy数组
a = np.array(list1)
print('数组', a)
# shape
print('形状(2,3)', a.shape)
# size
print('元素个数6', a.size)
# dim
print('维数，二维', a.ndim)

# 定义数据格式
b = np.array(list1, dtype=np.int32)
# 查看数据格式
print('数据格式', b.dtype)


"""
//**********************
**********************
定义特殊的数组
**********************
**********************//
"""
# 定义全为0的数组
print('2行3列全为0的数组', np.zeros((2, 3)))
# 定义全为1的数组
print('2行3列全为1的数组', np.ones((2, 3)))
# 定义空数组
print('2行3列空的数组', np.empty((2, 3)))
# 定义有序数组
print('起点1，终点11，步长2', np.arange(1, 12, 2))
print('起点0，终点11，步长1', np.arange(12))
# 定义随机数
print('11个随机数', np.random.random(11))
# 和arange差不多，只不过是自己确定步长
print('起点1，终点5，分段10段', np.linspace(1, 5, 10))
# 改变形状
print('将一维的', np.arange(12), '变成(3,4)的数组', np.arange(12).reshape(3, 4))