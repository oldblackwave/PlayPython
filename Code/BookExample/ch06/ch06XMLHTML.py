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

tables = doc.findall('.//table')
calls = tables[1]
puts = tables[2]

#print(calls.text_content())

rows = calls.findall('.//tr')

#print(rows[2].text_content())



def _unpack(row, kind='td'):
    elts = row.findall('.//%s' % kind)
    return [val.text_content() for val in elts]

print(_unpack(rows[0], kind='th'))
print(_unpack(rows[2], kind='td'))

print('\n')

def find_header_data():
    header = ['Strike']
    headerRow = _unpack(rows[0], kind='th')
    header.append(headerRow[1])
    return header

print(find_header_data())


    
    


def parse_options_data(table):
    rows = table.findall('.//tr')
    #header = _unpack(rows[0], kind='th')
    header = find_header_data()
    data = [_unpack(r, kind='td') for r in rows[2:]]
    return TextParser(data, names=header).get_chunk()

call_data = parse_options_data(calls)
put_data = parse_options_data(puts)

print(call_data[:10])









