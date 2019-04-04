import numpy as np
import pandas as pd


"""
//**********************
一、生成pandas
（1）pd.Series
（2）pd.DataFrame
**********************//
"""
a = pd.Series([1, 3, 6, 'orange'])
print('pandas和字典有点像', a)


# 生成6个日期行索引号
datas = pd.date_range('20190403', periods=6)
# 生成有6行4列行索引(index)和列索引(columns)的pandas
df = pd.DataFrame(np.random.random(size=(6, 4)), index=datas, columns=['a', 'b', 'c', 'd'])
print('生成有6行4列行索引(index)和列索引(columns)的pandas：\n', df)
# 以字典方式生成pandas，其中AB为列索引
df2 = pd.DataFrame({'A': 1, 'B': 2.}, index=np.arange(2))
print('以字典方式生成pandas\n', df2)


"""
//**********************
二、查看pandas数据类型
a.dtypes
**********************//
"""
print('df的数据类型\n', df.dtypes)


"""
//**********************
三、打印pandas的行索引号，列索引号，以及数值
**********************//
"""
print('行索引号', df.index)
print('列索引号', df.columns)
print('pandas数值', df.values)


"""
//**********************
四、pandas索引
（1）a.ix[]
（2）df.loc对标签进行索引
（3）df.iloc对位置进行索引
（4）df.ix标签和位置混合索引，不建议使用
**********************//
"""
print('选中df的a列\n', df['a'], df.loc[:, 'a'], df.iloc[:, 0])
print('选中df的第0行\n', df.iloc[0], df.loc['2019-04-03'])
print('选df的135行，12列', df.iloc[[1, 3, 5], 1:3], df.ix[[1, 3, 5], ['a', 'b']])
print('索引df的a列中大于0.5对应的行', df[df['a'] > 0.5])



"""
//**********************
五、pandas运算
（1）df.describe() 描述个数、均值、方差
（2）df.T 转置
（3）df.sort_index(axis=1,ascending=False)对行索引号排序，倒序
（4）df.sort_values(by='d')对d列的值进行排序
**********************//
"""
print('描述个数、均值、方差\n', df.describe())
print('转置\n', df.T)
print('对行索引号排序，倒序\n', df.sort_index(axis=1, ascending=False))
print('对d列的值进行排序\n', df.sort_values(by='d'))


"""
//**********************
六、通过索引改变pandas的值
**********************//
"""
# 将df的第二行第二列的值变为orange
df.iloc[2, 2] = 'orange'
print('将df的第二行第二列的值变为orange', df)
# 将df的第0行第0列的值变为apple
df.loc['2019-04-03', 'a'] = 'apple'
print('将df的第0行第0列的值变为apple', df)

# 将df的b列大于0.3对应的行令为0
df[df.b > 0.3] = 0
print('将df的b列大于0.3对应的行令为0', df)

# 将df的d列大于0.5对应的元素令为0
df.d[df.d > 0.5] = 0
df.d[df.d > 0.5] = 0
print('将df的d列大于0.5对应的元素令为0', df)

# 增加一列e和f
df['e'] = 6
df['f'] = np.nan
print('增加一列e和f', df)
# 增加一行
df3 = pd.DataFrame(np.arange(12).reshape(3, 4), columns=['a', 'b', 'x', 'y'])
s2 = pd.Series(np.arange(4), index=df3.columns)
res = df3.append(s2, ignore_index=True)
print(res)

"""
//**********************
六、pandas处理丢失数据（如nan数据）
**********************//
"""
# 直接丢掉nan所在的行或列(axis=1丢掉列,how='any'存在任意一个nan就丢，how='all'该列全部为nan才丢)
df1 = df.dropna(axis=1, how='any')
print('直接丢掉nan所在的列\n', df1)

# 填充nan的数据为0
df2 = df.fillna(value=0)
print('填充nan的数据为0\n', df2)

# 数据太多，怎么快速判断数据中是否有nan
print('丢失True, 未丢失False', df.isnull())
print('存在任一丢失数据，返回True\n', np.any(df.isnull()) == True)


