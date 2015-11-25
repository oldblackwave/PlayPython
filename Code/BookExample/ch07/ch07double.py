import numpy as np
import pandas as pd
import pandas.io.data as web
import sys
import csv
import json
import urllib

import pandas.io.data as web

from pandas import Series, DataFrame
from pandas.io.parsers import TextParser
from numpy import NaN as NA
from lxml.html import parse
from urllib.request import urlopen
from lxml import objectify
from io import StringIO

###############################################################

a = Series([np.nan, 2.5, np.nan, 3.5, 4.5, np.nan],
           index=['f','e','d','c','b','a'])
b = Series(np.arange(len(a), dtype=np.float64),
           index=['f','e','d','c','b','a'])

print(a)
print(b)
print('\n')

b[-1] = np.nan

print(a)
print(b)
print(np.where(pd.isnull(a),b,a))

print('\n')

print(b[:-2].combine_first(a[2:]))

print('\n')

df1 = DataFrame({'a':[1.,np.nan,5.,np.nan],'b':[np.nan,2.,np.nan,6],'c':range(2,18,4)})
df2 = DataFrame({'a':[5.,4.,np.nan,3.,7.],'b':[np.nan,3.,4.,6.,8.]})

print(df1)
print(df2)
print('\n')

print(df1.combine_first(df2))
print('\n')

data = DataFrame(np.arange(6).reshape(2,3), index=pd.Index(['Ohio','Colorado'], name='state'), columns=pd.Index(['one','two','three'], name='number'))
print(data)
print('\n')

result = data.stack()
print(result)
print('\n')
print(result.unstack())
print('\n')
print(result.unstack(0))
print('\n')
print(result.unstack('state'))
print('\n')

###############################################################

s1 = Series([0,1,2,3], index=['a','b','c','d'])
s2 = Series([4,5,6], index=['c','d','e'])

data2 = pd.concat([s1,s2], keys=['one','two'])
print(data2)
print('\n')
print(data2.unstack())
print('\n')
print(data2.unstack().stack())
print('\n')
print(data2.unstack().stack(dropna=False))
print('\n')

###############################################################

df = DataFrame({'left':result, 'right':result+5},columns=pd.Index(['left','right'], name='side'))

print(df)
print('\n')
print(df.unstack('state'))
print(df.unstack('state').stack('side'))
print('\n')

print(data[:10])
print('\n')








