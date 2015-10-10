import numpy as np
import pandas as pd

from pandas import Series, DataFrame



###############################################################

obj = Series([4,7,-5,3])
print(obj)
print(obj.index)
print(obj.values)

print('\n')
###############################################################

obj2 = Series([4,7,-5,3], index = ['d','b','a','c'])
print(obj2)
print(obj2.index)

print(obj2['a'])

obj2['d'] = 6
print(obj2['d'])

print(obj2[['c','a','d']])
print('\n')


###############################################################

print(obj2[obj2>0])
print(obj2*2)
print(np.exp(obj2))

print('\n')

print('b' in obj2)
print('e' in obj2)
###############################################################

sdata = {'Ohio':35000, 'Texas':71000, 'Oregon':16000, 'Utah':5000}
obj3 = Series(sdata)

print(obj3)

print('\n')
###############################################################

states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = Series(sdata, index=states)

print(obj4)
print('\n')

print(pd.isnull(obj4))
print(pd.notnull(obj4))

print('\n')

print(obj4.isnull())

print('\n')

###############################################################

print(obj3 + obj4)

print('\n')

obj4.name = 'population'

obj4.index.name = 'state'

print(obj4)

print('\n')
###############################################################

obj.index = ['Bob','Steve','Jeff','Ryan']
print(obj)

print('\n')
###############################################################

















