# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 14:04:12 2020

@author: BX
"""
import syllapy as slp
count=slp.count('ultimate');

import pandas as pd
import spacy

nlp=spacy.load("en_core_web_sm")
df = pd.read_csv( "DataWithTexts.csv" , index_col = 0)
df.head()
doc=nlp ("Hey let's see if I can make this sentence work properly, huh?")
for token in doc:
    if token.is_punct==False:
        print (slp.count (token.text))
        print (token)
def spw (doc):
    words=0
    syllables=0
    for token in doc:
            if token.is_punct==False:
                syllables=syllables+slp.count(token.text)
                words=words+1;
    return syllables/words
nlp=spacy.load("en_core_web_sm")
df = pd.read_csv( "DataWithTexts.csv" , index_col = 0)
df.head()
print(df.iloc[-1])
df['syl_per_word'] = df['docs'].apply( lambda x: spw(nlp(x)))
