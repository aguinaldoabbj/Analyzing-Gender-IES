# -*- coding: utf-8 -*-

import pandas as pd
import requests as requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint

from collections import Counter
import string


ufrn_employees_df = pd.read_csv('ufrn_employees_df.csv', index_col=False)

first_names = []
for name in ufrn_employees_df.Name:
    first_names.append(name.split()[0])
    
    
text = ','.join(first_names)

text_dict = Counter(text)