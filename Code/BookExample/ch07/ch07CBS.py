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

arr = np.arange(12).reshape((3,4))

print(arr)
print('\n')
print(np.concatenate([arr,arr], axis=1))
print('\n')

s1 = Series([0,1], index=['a','b'])
s2 = Series([2,3,4], index=['c','d','e'])
s3 = Series([5,6], index=['f','g'])

print(s1)
print(s2)
print(s3)

print('\n')
print(pd.concat([s1,s2,s3]))
print(pd.concat([s1,s2,s3], axis=1))
print('\n')

s4 = pd.concat([s1*5, s3])
print(s4)
print('\n')

print(pd.concat([s1,s4], axis=1))
print(pd.concat([s1,s4], axis=1, join='inner'))

print('\n')

print(pd.concat([s1, s4], axis=1, join_axes=[['a','c','b','e']]))

print('\n')

result = pd.concat([s1,s1,s3], keys=['one','two','three'])
print(result)
print('\n')
print(result.unstack())
print('\n')
print(pd.concat([s1,s2,s3], axis=1, keys=['one','two','three']))
print('\n')

df1 = DataFrame(np.arange(6).reshape(3,2), index=['a','b','c'],
                columns=['one', 'two'])
df2 = DataFrame(5+np.arange(4).reshape(2,2), index=['a','c',],
                columns=['three','four'])

print(df1)
print(df2)
print('\n')
print(pd.concat([df1,df2], axis=1, keys=['level1','level2']))
print('\n')

print(pd.concat({'level1':df1, 'level2':df2}, axis=1))

print('\n')

print(pd.concat([df1,df2], axis=1, keys=['level1','level2'],
                names= ['ipper','lower']))

print('\n')

df1 = DataFrame(np.random.randn(3,4), columns=['a','b','c','d'])
df2 = DataFrame(np.random.randn(2,3), columns=['b','d','a'])

print(df1)
print(df2)

print('\n')

print(pd.concat([df1,df2], ignore_index=True))

print('\n')



