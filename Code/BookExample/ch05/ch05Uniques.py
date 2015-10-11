import numpy as np
import pandas as pd

import pandas.io.data as web

from pandas import Series, DataFrame

###############################################################

obj = Series(['c','a','d','a','a','a','b','b','c','c'])

uniques = obj.unique()

print(uniques)
print('\n')

print(obj.value_counts())
print('\n')
print(pd.value_counts(obj.values,sort=False))

print('\n')

mask = obj.isin(['b','c'])
print(mask)
print(obj[mask])

print('\n')

###############################################################

data = DataFrame({'Qu1':[1,3,4,3,4],
                  'Qu2':[2,3,1,2,3],
                  'Qu3':[1,5,2,4,4]
                })

print(data)

result = data.apply(pd.value_counts).fillna(0)

print(result)

print('\n')


###############################################################

#Page 148

