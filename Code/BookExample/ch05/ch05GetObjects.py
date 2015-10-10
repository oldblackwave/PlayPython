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
