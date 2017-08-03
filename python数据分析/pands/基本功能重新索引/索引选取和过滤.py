#-*-coding:utf-8-*-
import numpy as np
from pandas import Series, DataFrame

print 'Series的索引，默认数字索引可以工作'
obj = Series(np.arange(4.), index=['a','b','c','d'])
print obj['b']
print obj[3]
print obj[[1,3]]
print[obj<2]
print

print 'Series的数组切片'
print obj['b':'c']
obj['b':'c'] = 5
print obj
print

print 'DataFrame的索引'
data = DataFrame(np.arange(16).reshape((4,4)),
                 index=['ohio','colorado','utah','new york'],
                 columns=['one','two','three','four']
                 )
print data
print data['two']
print data[['three','one']]
print data[:2]
print data.ix['colorado',['two','three']]
print data.ix[2]
print data.ix[:'utah','two']
print

print '根据条件选择'
print data[data.three>5]
print data<5
data[data<5] = 0
print data