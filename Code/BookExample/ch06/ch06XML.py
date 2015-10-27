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

###############################################################


path = 'data/Performance_MNR.xml'
parsed = objectify.parse(open(path))
root = parsed.getroot()

data = []
skip_fields = ['PARENT_SEQ', 'INDICATOR_SEQ', 'DESIRED_CHANGE', 'DECIMAL_PLACES']

for elt in root:
    el_data = {}
    for child in elt.getchildren():
        if child.tag in skip_fields:
            continue
        el_data[child.tag]=child.pyval
    data.append(el_data)
    
perf = DataFrame(data)
print(perf)



