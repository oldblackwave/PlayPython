import numpy as np
import pandas as pd

import pandas.io.data as web

from pandas import Series, DataFrame
from numpy import NaN as NA

###############################################################

string_data = Series(['aardvark','artichoke',np.nan,'avocado'])

print(string_data)
print('\n')
print(string_data.isnull())
print('\n')

string_data[0]=None
print(string_data.isnull())
print('\n')

###############################################################

data =Series([1,NA,3.5,NA,7])
print(data.dropna())

print('\n')

print(data[data.notnull()])

print('\n')

###############################################################

data = DataFrame([[1.,6.5,3.],
                 [1.,NA,NA],
                 [NA,NA,NA],
                 [NA,6.5,3.]]
                 )

cleaned = data.dropna()
print(data)
print('\n')
print(cleaned)
print('\n')
print(data.dropna(how='all'))
print('\n')

data[4] = NA
print(data)
print('\n')
print(data.dropna(axis=1, how='all'))
print('\n')



###############################################################

df = DataFrame(np.random.randn(7,3))
df.ix[:4, 1] = NA
df.ix[:2, 2] = NA

print(df)
print('\n')
print(df.dropna(thresh=3))
print('\n')

print(df.fillna(0))
print('\n')

print(df.fillna({1:0.5, 3:-1}))
print('\n')

_ = df.fillna(0, inplace=True)
print(df)
print('\n')

###############################################################

df = DataFrame(np.random.randn(6,3))
df.ix[2:, 1]=NA 
df.ix[4:, 2]=NA

print(df)
print('\n')
print(df.fillna(method='ffill'))
print('\n')
print(df.fillna(method='ffill', limit=2))
print('\n')

###############################################################

data = Series([1.,NA,3.5,NA,7])

print(data.fillna(data.mean()))
print('\n')

###############################################################

data = Series(np.random.randn(10),
              index = [['a','a','a','b','b','b','c','c','d','d'],
                       [1,2,3,1,2,3,1,2,2,3]])


print(data)
print('\n')
print(data.index)
print('\n')
print(data['b'])
print('\n')
print(data['b':'c'])
print('\n')
print(data.ix[['b','d']])
print('\n')
print(data[:,2])
print('\n')
print(data.unstack())
print('\n')
print(data.unstack().stack())
print('\n')

###############################################################

#page 154

frame = DataFrame(np.arange(12).reshape((4,3)),
                  index = [['a','a','b','b'],[1,2,1,2]],
                  columns = [['Ohio', 'Ohio', 'Colorado'],['Green','Red','Green']]
                  )

print(frame)
print('\n')

frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'color']

print(frame)
print('\n')

###############################################################

'''
MultiIndex.from_arrays([['Ohio','Ohio','Colorado'],['Green','Red','Green']],
                        names = ['state','color'])
'''
###############################################################

print(frame.swaplevel('key1', 'key2'))
print('\n')
print(frame.sortlevel(1))
print('\n')
print(frame.sortlevel(0))
print('\n')
print(frame.swaplevel(0, 1).sortlevel(0))
print('\n')

###############################################################

print(frame.sum(level='key2'))
print('\n')
print(frame.sum(level='color',axis=1))
print('\n')

###############################################################



































