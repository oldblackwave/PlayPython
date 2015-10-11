import numpy as np
import pandas as pd

from pandas import Series, DataFrame

###############################################################

s1 = Series([7.3,-2.5,3.4,1.5], index=['a','c','d','e'])
s2 = Series([-2.1,3.6,-1.5,4,3.1], index=['a','c','e','f','g'])

print(s1)
print(s2)

print(s1+s2)
print('\n')
###############################################################

df1 = DataFrame(np.arange(9.).reshape((3,3)),
                columns = list('bcd'),
                index = ['Ohio', 'Texas', 'Colorado']
                )

df2 = DataFrame(np.arange(12.).reshape((4,3)),
                columns = list('bde'),
                index = ['Utah', 'Ohio', 'Texas', 'Oregon']
                )

print(df1)
print(df2)

print('\n')

print(df1+df2)

print('\n')

###############################################################

df1 = DataFrame(np.arange(12.).reshape((3,4)), columns=list('abcd'))
df2 = DataFrame(np.arange(20.).reshape((4,5)), columns=list('abcde'))

print(df1)
print(df2)

print('\n')
print(df1+df2)
print(df1.reindex(columns=df2.columns, fill_value=0))
print('\n')

###############################################################

arr = np.arange(12.).reshape((3,4))
print(arr)
print(arr[0])
print('\n')
print(arr - arr[0])
print('\n')


###############################################################

frame = DataFrame(np.arange(12.).reshape((4,3)),
                  columns = list('bde'),
                  index = ['Utah', 'Ohio', 'Texas', 'Oregon']
                  )

print(frame)
print('\n')

series = frame.ix[0]
print(series)
print('\n')

print(frame - series)
print('\n')

series2 = Series(range(3), index=['b','e','f'])
print(series2)
print(frame + series2)

print('\n')

series3 = frame['d']
print(frame)
print(series3)

print('\n')

print(frame.sub(series3, axis=0))


























