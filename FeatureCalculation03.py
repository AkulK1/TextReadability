# -*- coding: utf-8 -*-

import pandas as pd
import spacy
from spacy_syllables import SpacySyllables

nlp = spacy.load("en_core_web_sm")
syllables = SpacySyllables(nlp)
nlp.add_pipe(syllables, after="tagger")

df = pd.read_csv( "Data03.csv" , index_col = 0)

def plot_graph( feat ):
    df.plot( x=feat, y='difficulty', style='o')

df['flesch_score'] = 206.835 - 1.015*df['ws_per_sents'] -84.6*df['syl_per_word']
plot_graph('flesch_score')

df['ari_score'] = 4.71*df['avg_wd_length']+0.5*df['ws_per_sents']
plot_graph('ari_score')

def calc_dale( row ):
    dw =row['not_easy_words']
    wps = row['ws_per_sents']
    res = 0.1579*(dw*100) + 0.0496*wps
    if dw > 0.05:
        res+=3.6365
    return res

df['dale_score'] = df.apply( lambda row: calc_dale(row), axis =1  )
plot_graph('dale_score')
plot_graph('not_easy_words')

#SMOG Index
import math

df['SMOG'] = 3+df['polysyls'].apply (lambda x: math.sqrt(x))
df.plot( x = 'SMOG', y = 'difficulty', style = 'o' ) 

#gunning fog
df['gunning_fog'] = 0.4*(df['ws_per_sents']+df['not_easy_words'])
df.plot( x = 'gunning_fog', y = 'difficulty', style = 'o' ) 

#CLI
df['CLI'] = 0.0588*100*df['avg_wd_length']-0.296*(df['sentences']/df['ws']*100)-15.8
df.plot( x = 'CLI', y = 'difficulty', style = 'o' ) 

#correlation with difficulty
for col1 in df.columns:
    if df[col1].dtypes in ["int64", 'float64' ]:
        print( col1, df[col1].corr( df['difficulty'] ))
        
dale_df = df[['title', 'difficulty','not_easy_words','ws_per_sents','dale_score']]
