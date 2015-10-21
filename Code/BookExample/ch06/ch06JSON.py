import numpy as np
import pandas as pd
import pandas.io.data as web
import sys 
import csv
import json

import pandas.io.data as web

from pandas import Series, DataFrame
from numpy import NaN as NA

###############################################################

obj = """
    {"name":"Wes",
    "places_lived":["United States","Spain","Germany"],
    "pet":null,
    "siblings":[{"name":"Scott", "age":25, "pet":"Zuko"},
                {"name":"Katie", "age":33, "pet":"Cisco"}
                ]
     }
    """

result = json.loads(obj)

print(result)

print('\n')

asjson = json.dumps(result)

siblings = DataFrame(result['siblings'], columns=['name', 'age'])

print(siblings)

print('\n')



###############################################################


