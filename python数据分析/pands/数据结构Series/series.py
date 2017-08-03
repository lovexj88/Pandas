#-*-coding:utf-8-*-
from pandas import Series

print '用数组生成Series'
obj = Series([4,7,-5,3])
print obj
print obj.index
print obj.values
print

print'指定Series的index'
obj2 = Series([4,7,-5,3], index=['d','b','a','c'])
print obj2
print obj2.index
print obj2['a']
obj2['d']=6
print obj2[['c','a','d']]
print obj2[obj2>0]
print 'b' in obj2
print 'e' in obj2
print

print '使用字典生成Series'
sdata = {'ohio':45000,'texas':71000,'oregon':16000,'utah':5000}
obj3 = Series(sdata)
print obj3
print

print '使用字典生成Series,并额指定index,不匹配部分为NaN'
states = ['california','ohio','oregon','texas']
obj4 = Series(sdata, index=states)
print obj4
print

print 'Series相加，相同索引部分相加。'
print obj3+obj4
print

print '指定Series及索引的名字'
obj4.name = 'population'
obj4.index.name = 'state'
print obj4
print

print '替换index'
obj.index = ['bob','steve','jeff','ryan']
print obj