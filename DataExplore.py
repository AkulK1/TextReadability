# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 13:12:23 2020

@author: kesar
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

df = pd.read_csv( "no_text.csv",  index_col = 0)
df_s = df[['titles' , 'difficulty', 'sci_info', 'flesch_score', 'linsear', 'dale_score']]
df_s = df_s.sort_values( by= ['difficulty', 'linsear'])
