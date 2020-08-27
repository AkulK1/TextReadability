
# -*- coding: utf-8 -*-
"""
This snipet is from Ken Jee's github'
"""

import requests 
from data_input import dt_in

URL = 'https://txt-readability-20.herokuapp.com/predict'
headers = {"Content-Type": "application/json"}
data = {"input": dt_in}

r=requests.get(URL, headers=headers, json=data)

print (r.json() )