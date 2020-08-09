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



#ff = open( 'TextData/b168_DreaminginCuban.txt', 'r', encoding="utf8" )



def get_nlp( str ):
    ff = open( 'TextData/' + str, 'r', encoding = 'utf8', errors = 'ignore' )
    print( str )
    return ff.read()


df['docs'] = df['text'].apply( get_nlp )
df.to_csv( "DataWithTexts.csv" )
# for doc in df['docs']:
#     print( len(list(doc.sents)) )