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


left1 = DataFrame({'key':['a','b','a','a','b','c'],
                   'value':range(6)})
right1 = DataFrame({'group_val':[3.5,7]}, index=['a','b'])

print(left1)
print(right1)
print('\n')

print(pd.merge(left1, right1, left_on='key', right_index=True))
print('\n')
print(pd.merge(left1, right1, left_on='key', right_index=True, how='outer'))
print('\n')

lefth = DataFrame({'key1':['Ohio','Ohio','Ohio','Nevada','Nevada'],
                   'key2':[2000,2001,2002,2001,2002],
                   'data':np.arange(5.)})

righth = DataFrame(np.arange(12).reshape((6,2)),
                   index=[['Nevada','Nevada','Ohio','Ohio','Ohio','Ohio'],[2001,2000,2000,2000,2001,2002]],
                   columns=['event1','event2'])

print(lefth)
print(righth)
print('\n')

print(pd.merge(lefth, righth, left_on=['key1','key2'], right_index=True))
print('\n')
print(pd.merge(lefth, righth, left_on=['key1','key2'], right_index=True, how='outer'))
print('\n')

left2 = DataFrame([[1.,2.],[3.,4.],[5.,6.]], index=['a','c','e'],columns=['Ohio','Nevada'])
right2 = DataFrame([[7.,8.],[9.,10.],[11.,12.],[13,14]],
                   index = ['b','c','d','e'], columns=['Missouri','Alabama'])

print(left2)
print(right2)
print('\n')





