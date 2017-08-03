#-*-coding:utf-8-*-
import numpy as np
from pandas import Series, DataFrame

print'根据索引排序，对于DataFrame可以指定轴'
obj = Series(range(4),index=['d','a','b','c'])
print obj.sort_index()
frame = DataFrame(np.arange(8).reshape((2,4)),
                  index=['three','one'],
                  columns=list('dabc'))
print frame.sort_index()
print frame.sort_index(axis=1)
print frame.sort_index(axis = 1,ascending=False)#降序
print

print'根据值排序'
obj = Series([4,7,-3,2])
print obj.sort_values()
print

print 'DataFrame指定列排序'
frame = DataFrame({'b':[4,7,-3,2],'a':[0,1,0,1]})
print frame
print frame.sort_values(by='b')
print frame.sort_values(by=['a','b'])

print 'rank,求排名的平均位置'
obj = Series([7,-5,7,4,2,0,4])
print obj.rank()
print obj.rank(method='first')
print obj.rank(ascending=False,method='max')
frame = DataFrame({'b':[4.3,7,-3,2],
                   'a':[0,1,0,1],
                   'c':[-2,5,8,-2.5]})
print frame
print frame.rank(axis=1)

