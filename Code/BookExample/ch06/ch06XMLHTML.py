import numpy as np
import pandas as pd
import pandas.io.data as web
import sys 
import csv
import json
import urllib

import pandas.io.data as web

from pandas import Series, DataFrame
from numpy import NaN as NA
from lxml.html import parse
from urllib.request import urlopen


###############################################################

parsed = parse(urlopen('http://finance.yahoo.com/q/op?s=AAPL+Options'))

#print(parsed)
#print('\n')

doc = parsed.getroot()
#print(doc)
links = doc.findall('.//a')

print(links[15:20])
print('\n')

lnk = links[28]
print(lnk)
print('\n')

print(lnk.get('href'))
print(lnk.text_content())
print('\n')

###############################################################


urls = [lnk.get('href') for lnk in doc.findall('.//a')]
print(urls[0:10])

print('\n')

tables = doc.findall('.//tr')
calls = tables[9]
puts = tables[13]

print(calls.text_content())

rows = calls.findall('.//tr')

'''
def _unpack(row, kind='td'):
    elts = row.findall('.//%s' % kind)
    return [val.text_content() for val in elts]

print(_unpack(rows[1], kind='td'))
'''













