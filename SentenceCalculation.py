# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 14:04:12 2020

@author: kesar
"""


import pandas as pd
import spacy

nlp = spacy.load("en_core_web_sm")

df = pd.read_csv( "DataWithTexts.csv" , index_col = 0)

df.head()
print(df.iloc[-1])


df['sentences'] = df['docs'].apply( lambda x: len(list(nlp(x).sents)))
df['nlps'] = df['docs'].apply( lambda x: nlp(x))

