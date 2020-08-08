import pandas as pd

df = pd.read_csv( "BookDataForMLTextComplexityProject.csv" )
print( df.head() )

print(df.columns)
print(df['difficulty'].value_counts())


print(df[['text', 'difficulty']])

import spacy

nlp = spacy.load("en_core_web_sm")

#ff = open( 'TextData/b168_DreaminginCuban.txt', 'r', encoding="utf8" )



def get_nlp( str ):
    ff = open( 'TextData/' + str, 'r', encoding = 'utf8', errors = 'ignore' )
    print(str)
    return nlp(ff.read())


df['docs'] = df['text'].apply( get_nlp )
