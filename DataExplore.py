# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 13:12:23 2020

@author: kesar
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

df = pd.read_csv( "no_text.csv" )

def calc_dale( row ):
    dw =row['not_easy_words']
    wps = row['ws_per_sents']
    res = 0.1579*(dw*100) + 0.0496*wps
    return res
df['dale_score'] = df.apply( lambda row: calc_dale(row), axis =1  )



df_s = df[['titles' , 'difficulty', 'sci_info', 'flesch_score', 'linsear', 'dale_score']]


from statistics import mean
from statistics import stdev
df_fk = df_s.groupby(['difficulty']).flesch_score.agg( [mean, stdev] )

def z_score( row ):
    diff = row['difficulty']
    print(df_fk.loc[diff])
    m =  df_fk.loc[diff]['mean']
    st = df_fk.loc[diff]['stdev']
    
    fs= row['flesch_score']
    print( fs, m, st)
    return ( fs- m)/st

df_l = df_s.groupby(['difficulty']).linsear.agg( [mean, stdev] )
def z_score2( row ):
    diff = row['difficulty']
    print(df_l.loc[diff])
    m =  df_l.loc[diff]['mean']
    st = df_l.loc[diff]['stdev']
    
    fs= row['linsear']
    print( fs, m, st)
    return ( fs- m)/st

df_d = df_s.groupby(['difficulty']).dale_score.agg( [mean, stdev] )
def z_score3( row ):
    diff = row['difficulty']
    print(df_d.loc[diff])
    m =  df_d.loc[diff]['mean']
    st = df_d.loc[diff]['stdev']
    
    fs= row['dale_score']
    print( fs, m, st)
    return ( fs- m)/st


df_s[ 'z_fk' ] = df_s.apply( lambda row: z_score( row ),  axis =1) 
df_s['z_l']=df_s.apply( lambda row: z_score2( row ),  axis =1) 
df_s['z_d'] = df_s.apply( lambda row: z_score3( row ),  axis =1) 

df_s = df_s.sort_values( by= ['difficulty', 'dale_score'])

zscores = df_s

print( zscores )
