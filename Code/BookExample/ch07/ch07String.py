import numpy as np
import pandas as pd
import pandas.io.data as web
import sys
import csv
import json
import urllib
import re

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

text = "foo   bar\t baz   \tqux"

print(re.split('\s+',text))

regex = re.compile('\s+')

print(regex.split(text))

print(regex.findall(text))

print('\n')
###############################################################

text = """ Dave dave@google.com
Steve steve@gmail.com
Rob rob@gmail.com
Ryan ryan@yahoo.com
"""

pattern = r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'

regex = re.compile(pattern, flags=re.IGNORECASE)
print(regex.findall(text))

print('\n')

m = regex.search(text)
print(m)

print(text[m.start():m.end()])
print(regex.match(text))
print(regex.sub('REDACTED',text))

pattern = r'([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})'
regex = re.compile(pattern, flags=re.IGNORECASE)

m = regex.match('wesm@bright.net')

print(m.groups())

print(regex.findall(text))

m = regex.match('wesm@bright.net')

print(m.groupdict())

