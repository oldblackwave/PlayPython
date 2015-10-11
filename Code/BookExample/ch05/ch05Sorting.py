import numpy as np
import pandas as pd

from pandas import Series, DataFrame

###############################################################

obj = Series(range(4), index=['d','a','b','c'])
print(obj.sort_index())

print('\n')

frame = DataFrame(np.arange(8).reshape((2,4)),
                  index=['three','one'],
                  columns=['d','a','b','c']
                  )

print(frame)
print('\n')
print(frame.sort_index())
print('\n')
print(frame.sort_index(axis=1))
print('\n')
print(frame.sort_index(axis=1,ascending=False))
print('\n')

###############################################################

obj = Series([4,7,-3,2])
print(obj.order())
print('\n')

obj = Series([4, np.nan, 7, np.nan, -3, 2])
print(obj.order())
print('\n')

###############################################################

frame = DataFrame({'b':[4,7,-3,2],
                   'a':[0,1,0,1]
                   })
print(frame)
print(frame.sort_index(by='b'))
print(frame.sort_index(by=['a','b']))
print('\n')

###############################################################

obj = Series([7,-5,7,4,2,0,4])
print(obj)
print(obj.rank())
print(obj.rank(method='first'))
print(obj.rank(ascending=False, method='max'))
print('\n')

frame = DataFrame({'b':[4.3,7,-3,2],'a':[0,1,0,1],'c':[-2,5,8,-2.5]})

print(frame)
print(frame.rank())
print(frame.rank(axis=1))

print('\n')

###############################################################

obj = Series(range(5),index=['a','a','b','b','c'])
print(obj)
print(obj.index.is_unique)

print('\n')

print(obj['a'])
print(obj['c'])

###############################################################


df = DataFrame(np.random.randn(4,3), index=['a','a','b','b'])

print(df)
print(df.ix['b'])

print('\n')

