import numpy as np
import pandas as pd

from pandas import Series, DataFrame

###############################################################

obj = Series(range(3), index = ['a','b','c'])
index = obj.index

print(index)
print(index[1:])

print('\n')


###############################################################

index = pd.Index(np.arange(3))
obj2 = Series([1.5,-2.5,0],index=index)

print(obj2.index is index)

print('\n')

###############################################################

obj = Series([4.5,7.2,-5.3,3.6],index=['d','b','a','c'])

obj2 = obj.reindex(['a','b','c','d','e'])

print(obj2)

print('\n')

print(obj.reindex(['a','b','c','d','e'], fill_value=0))

print('\n')

obj3 = Series(['blue','purple','yellow'],index=[0,2,4])
print(obj3.reindex(range(6),method='ffill'))

print('\n')

###############################################################

frame = DataFrame(np.arange(9).reshape((3,3)), index=['a','c','d'], columns=['Ohio','Texas','California'])

print(frame)
print('\n')

frame2 = frame.reindex(['a','b','c','d'])
print(frame2)
print('\n')

###############################################################

states = ['Texas','Utah','California']

print(frame.reindex(columns=states))

print('\n')

print(frame.reindex(index=['a','b','c','d'], method='ffill', columns=states))

print(frame.ix[['a','b','c','d'],states])

print('\n')

###############################################################

obj = Series(np.arange(5.), index=['a','b','c','d','e'])

new_obj = obj.drop('c')

print(new_obj)

print('\n')

print(obj.drop(['d','c']))

print('\n')

###############################################################

data = DataFrame(np.arange(16).reshape((4,4)),
                 index = ['Ohio', 'Colorado', 'Utah', 'New York'],
                 columns = ['one','two','three','four']
                 )

print(data.drop(['Colorado', 'Ohio']))
print('\n')

print(data.drop('two', axis=1))
print('\n')
print(data.drop(['two','four'],axis=1))
print('\n')







































