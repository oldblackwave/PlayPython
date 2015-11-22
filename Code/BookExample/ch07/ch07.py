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

df1 = DataFrame({'key':['b','b','a','c','a','a','b'],
                 'data1':range(7)})
df2 = DataFrame({'key':['a','b','d'],
                 'data2':range(3)})

print(df1)
print('\n')
print(df2)
print('\n')

print(pd.merge(df1,df2))

print('\n')

print(pd.merge(df1,df2,on='key'))
print('\n')

###############################################################

df3 = DataFrame({'lkey':['b','b','a','c','a','a','b'],
                'data1':range(7)})

df4 = DataFrame({'rkey':['a','b','d'],
                 'data2':range(3)})

print(df3)
print('\n')
print(df4)
print('\n')

print(pd.merge(df3, df4, left_on='lkey', right_on='rkey'))

print('\n')












