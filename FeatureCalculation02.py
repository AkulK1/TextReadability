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


       
#count principal modal verbs
def count_Modals (x):
    count=0
    mdls= set ()
    mdls.add ('Can')
    mdls.add ('can')
    mdls.add ('Could')
    mdls.add ('could')
    mdls.add ('May')
    mdls.add ('may')
    mdls.add ('Might')
    mdls.add ('might')
    mdls.add ('Will')
    mdls.add ('will')
    mdls.add ('Would')
    mdls.add ('would')
    mdls.add ('Must')
    mdls.add ('must')
    mdls.add ('Shall')
    mdls.add ('shall')
    mdls.add ('Should')
    mdls.add ('should')
    for token in x:
        if (token.lemma_ in mdls):
            count+=1;
    return count


df['modals_per_sent'] = df['docs'].apply( lambda x: count_Modals(nlp(x)))/df['sentences']

df.plot( x = 'modals_per_sent', y = 'difficulty', style = 'o' )

from collections import Counter
df['c'] = df['docs'].apply( lambda x: Counter( token.pos_ for token in nlp(x) ) )

df['adj']  = df['c'].apply( lambda x: x['ADJ'] )/df['sentences']      
df.plot( x = 'adj', y = 'difficulty', style = 'o' )    
    
df['verb']  = df['c'].apply( lambda x: x['VERB'] )/df['sentences'] 
df.plot( x = 'verb', y = 'difficulty', style = 'o' )        

df['adp']  = df['c'].apply( lambda x: x['ADP'] )/df['sentences']      
df.plot( x = 'adp', y = 'difficulty', style = 'o' )        

df['adv']  = df['c'].apply( lambda x: x['ADV'] )/df['sentences'] 
df.plot( x = 'adv', y = 'difficulty', style = 'o' ) 

df['sconj']  = df['c'].apply( lambda x: x['SCONJ'] )/df['sentences'] 
df.plot( x = 'sconj', y = 'difficulty', style = 'o' ) 

df['cconj']  = df['c'].apply( lambda x: x['CCONJ'] )/df['sentences'] 
df.plot( x = 'cconj', y = 'difficulty', style = 'o' ) 

df['aux']  = df['c'].apply( lambda x: x['AUX'] )/df['sentences'] 
df.plot( x = 'aux', y = 'difficulty', style = 'o' ) 

df['det']  = df['c'].apply( lambda x: x['DET'] )/df['sentences'] 
df.plot( x = 'det', y = 'difficulty', style = 'o' ) 

#correlation with difficulty
for col1 in df.columns:
    if df[col1].dtypes in ["int64", 'float64' ]:
        print( col1, df[col1].corr( df['difficulty'] ))