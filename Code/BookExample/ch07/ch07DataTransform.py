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

data = DataFrame({'k1':['one'] * 3 + ['two'] * 4,
                  'k2':[1,1,2,3,3,4,4]})

print(data)
print('\n')

print(data.duplicated())
print('\n')

print(data.drop_duplicates())
print('\n')

data['v1'] = range(7)
print(data.drop_duplicates(['k1']))
print('\n')

print(data.drop_duplicates(['k1','k2'], take_last=True))
print('\n')

data = DataFrame({'food':['bacon','pulled pork','bacon','Pastrami','corned beef','Bacon','pastrami','honey ham','nova lox'],
                  'ounces':[4,3,12,6,7.5,8,3,5,6]})
print(data)
print('\n')

meat_to_animal = {'bacon':'pig',
                  'pulled pork':'pig',
                  'pastrami':'cow',
                  'corned beef':'cow',
                  'honey ham':'pig',
                  'nova lox':'salmon'}

data['animal'] = data['food'].map(str.lower).map(meat_to_animal)
print(data)
print('\n')

print(data['food'].map(lambda  x:meat_to_animal[x.lower()]))
print('\n')

data = Series([1.,-999.,2.,-999.,-1000.,3.])
print(data)
print('\n')

print(data.replace(-999,np.nan))
print(data.replace([-999,-1000],np.nan))
print(data.replace([-999,-1000],[np.nan, 0]))
print(data.replace({-999:np.nan, -1000:0}))

print('\n')

###############################################################

data = DataFrame(np.arange(12).reshape((3,4)),
                 index=['Ohio','Colorado','New York'],
                 columns=['one','two','three','four'])
print(data)
print('\n')

print(data.index.map(str.upper))
print('\n')

data.index = data.index.map(str.upper)
print(data)
print('\n')

print(data.rename(index=str.title, columns=str.upper))
print('\n')

print(data.rename(index={'OHIO':'INDIANA'},columns={'three':'peekaboo'}))
print('\n')

_ = data.rename(index={'OHIO':'INDIANA'}, inplace=True)
print(data)

print('\n')



