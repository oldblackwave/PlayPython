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

val = 'a,b, guido'
print(val.split(','))
print('\n')

pieces = [x.strip() for x in val.split(',')]
print(pieces)
print('\n')

first, second, third = pieces
print(first + '::'+ second + '::' + third)
print('::'.join(pieces))

print('\n')

print('guido' in val)
print(val.index(','))

print(val.find(':'))
##print(val.index(':'))
print(val.count(','))
print(val.replace(',', '::'))
print(val.replace(',',''))
print('\n')

###############################################################

