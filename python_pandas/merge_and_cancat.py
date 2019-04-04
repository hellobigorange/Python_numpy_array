import numpy as np
import pandas as pd

"""
//**********************
九、行列标签相同排序
**********************//
"""
df1 = pd.DataFrame(np.ones((3, 4)), columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.ones((3, 4))*2, columns=['a', 'b', 'c', 'd'])
df3 = pd.DataFrame(np.ones((3, 4))*3, columns=['a', 'b', 'c', 'd'])

# 竖向合并,ignore_index=True忽略原来的列索引号,重新拍序
res = pd.concat([df1, df2, df3], axis=0, ignore_index=True)
print('竖向合并\n', res)


"""
//**********************
九、行列标签不同相同合并
（1）pd.concat([df4, df5]):直接合并，对方没有的行列补Nan
（2）pd.concat([df4, df5], join='inner')只合并二者共有的行列
（3）pd.concat([df4, df5], axis=1, join_axes=[df4.index])横向合并，按df4的index标签合并，df2没有补Nan
（4）pd.append()
**********************//
"""
df4 = pd.DataFrame(np.ones((3, 4)), columns=['a', 'b', 'c', 'd'], index=[1, 2, 3])
df5 = pd.DataFrame(np.ones((3, 4))*2, columns=['b', 'c', 'd', 'e'], index=[2, 3, 4])
res1 = pd.concat([df4, df5])
res2 = pd.concat([df4, df5], join='inner')
res3 = pd.concat([df4, df5], axis=1, join_axes=[df4.index])
print(res1, '\n',  res2, '\n', res3)

# 在df4的后面缀上df5,纵向合
df6 = pd.DataFrame(df5.values, index=df4.index, columns=df4.columns)
res4 = df4.append([df6, df5], ignore_index=True)
print(res4)
# 增加一行
df3 = pd.DataFrame(np.arange(12).reshape(3, 4), columns=['a', 'b', 'x', 'y'])
s2 = pd.Series(np.arange(4), index=df3.columns)
res5 = df3.append(s2, ignore_index=True)
print(res5)


"""
//**********************
十、merge合并
（1）pd.merge()
**********************//
"""
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'C': ['C0', 'C1', 'C2', 'C3'],
                     'D': ['D0', 'D1', 'D2', 'D3']})
# 以key的columns为基准合并
res6 = pd.merge(left, right, on='key')
print(res6)
# 考虑有两个key
left1 = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                      'key2': ['K0', 'K1', 'K0', 'K1'],
                      'A': ['A0', 'A1', 'A2', 'A3'],
                      'B': ['B0', 'B1', 'B2', 'B3']})
right1 = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                       'C': ['C0', 'C1', 'C2', 'C3'],
                       'D': ['D0', 'D1', 'D2', 'D3']})
# how='inner'合并key1key2都相同的，how='outer'都合并，没有补nan
res7 = pd.merge(left1, right1, on=['key1', 'key2'], how='inner')
print(res7)

# 以key为基准合并，但考虑相同索引可能背后意义不同，故予以分别显示、
boys = pd.DataFrame({'K': ['K0', 'K1', 'K2'],
                     'age': [1, 2, 3]})
girls = pd.DataFrame({'K': ['K0', 'K0', 'K3'],
                     'age': [4, 5, 6]})
res9 = pd.merge(boys, girls, on='K', suffixes=['boy_age', 'girl_age'], how='inner')
print(res9)
