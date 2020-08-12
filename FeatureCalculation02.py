# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 15:39:42 2020

@author: kesar
"""

import pandas as pd
import spacy
from spacy_syllables import SpacySyllables

nlp = spacy.load("en_core_web_sm")
syllables = SpacySyllables(nlp)
nlp.add_pipe(syllables, after="tagger")

df = pd.read_csv( "Data02.csv" , index_col = 0)

def calc_polysyls( doc ):
    count  = 0
    for token in doc:
        syl1 = token._.syllables_count
        if  syl1 != None and syl1 > 2:
            count+=1
    print( count )
    return count

df['polysyls'] = df['docs'].apply( lambda x: calc_polysyls(nlp(x)) )/df['ws']

df.plot( x = 'polysyls', y = 'difficulty', style = 'o' )

def calc_monosyls( doc ):
    count  = 0
    wss = 0
    for token in doc:
        syl1 = token._.syllables_count
        if  syl1 != None:
            wss+=1
            if syl1 == 1:
                count+=1
    print( count/wss )
    return count/wss
df['monosyls'] = df['docs'].apply( lambda x: calc_monosyls( nlp(x) ))
df.plot( x = 'monosyls', y = 'difficulty', style = 'o' )

for col1 in df.columns:
    if df[col1].dtypes in ["int64", 'float64' ]:
        print( col1, df[col1].corr( df['difficulty'] ))
