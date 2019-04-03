import numpy as np

# 浅拷贝，拷贝后地址相同，一个改变，其他的也会改变。 a is b，判断a,b是否完全相同

a = np.arange(12).reshape(3, 4)
b = a
a[0] = 3
print(a == b, a is b)


# 深拷贝拷贝，拷贝后地址不同，一个改变，其他的不会变

c = np.copy(a)
a[1] = 3
print(a == c, a is c)