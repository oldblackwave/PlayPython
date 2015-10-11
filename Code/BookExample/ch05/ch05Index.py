import numpy as np
import pandas as pd

from pandas import Series, DataFrame

###############################################################

obj = Series(np.arange(4.), index = ['a','b','c','d'])

print(obj['b'])
print(obj[1])
print(obj[2:4])
print(obj[['b','a','d']])
print(obj[[1,3]])
print(obj[obj<2])
print(obj['b':'c'])

obj['b':'c'] = 5
print(obj)

print('\n')

###############################################################

data = DataFrame(np.arange(16).reshape((4,4)),
                 index = ['Ohio', 'Colorado', 'Utah', 'New York'],
                 columns = ['one','two','three','four']
                 )

print(data)
print(data['two'])
print(data[['three','one']])
print(data[:2])
print(data[data['three']>5])
print(data<5)
print('\n')
data[data<5] = 0
print(data)
print('\n')
print(data.ix['Colorado',['two','three']])
print(data.ix[['Colorado','Utah'],[3,0,1]])
print(data.ix[2])
print(data.ix[:'Utah','two'])
print(data.ix[data.three > 5,:3])
print('\n')
print(data[0:1])










