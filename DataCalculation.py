# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 14:43:49 2020

@author: kesar
"""


import pandas as pd

df = pd.read_csv( "BookDataForMLTextComplexityProject.csv" )
print( df.head() )

print(df.columns)
print(df['difficulty'].value_counts())


print(df[['text', 'difficulty']])
