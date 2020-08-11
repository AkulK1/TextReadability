import pandas as pd
import spacy
from spacy_syllables import SpacySyllables

#reading from the csv file
nlp = spacy.load("en_core_web_sm")
syllables = SpacySyllables(nlp)
nlp.add_pipe(syllables, after="tagger")
df = pd.read_csv( "DataWithTexts.csv" , index_col = 0)
df.head()
print(df.iloc[-1])

#compute the number of sentences in each sample text
df['sentences'] = df['docs'].apply( lambda x: len(list(nlp(x).sents)))
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

##count the number of words in each sample text
def wordCount (doc):
    ws =0
    for token in doc:
        if token._.syllables_count != None:
            ws+=1
    return ws;
df['ws'] = df['docs'].apply( lambda x: wordCount(nlp(x)))

#compute the average sentence length
df['ws_per_sents'] = df['ws']/df['sentences']
df.to_csv( "updatedFeatures.csv" )



