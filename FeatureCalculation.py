# -*- coding: utf-8 -*-



import pandas as pd
import spacy
from spacy_syllables import SpacySyllables

nlp = spacy.load("en_core_web_sm")
syllables = SpacySyllables(nlp)
nlp.add_pipe(syllables, after="tagger")


df = pd.read_csv( "DataWithTexts.csv" , index_col = 0)

df.head()
print(df.iloc[-1])

df['sentences'] = df['docs'].apply( lambda x: len(list(nlp(x).sents)))

doc1 =nlp ("Hey let's see if I can make this sentence work properly, huh?")
for token in doc1:
    print( token.text, token._.syllables_count )
    
def spw (doc):
    ws =0
    syls =0
    for token in doc:
        if token._.syllables_count != None:
            ws+=1
            syls+=token._.syllables_count
    print( syls/ws )
    return syls/ws

df['syl_per_word'] = df['docs'].apply( lambda x: spw(nlp(x)) )


df.plot( x = 'syl_per_word', y = 'difficulty', style = 'o' )
