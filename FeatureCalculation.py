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

df.plot(x= 'ws_per_sents', y ='difficulty',style = 'o')


ff = open('EasyWordList.txt', 'r')
easy_words = [i.lower() for i in ff.read().split()]


def f_not_easy_words( doc ):
    res = 0
    for token in doc:
        t1 =  token.lemma_
        t1 = t1.lower()
        
        if (token._.syllables_count != None) and not ( (token.text.lower() in easy_words) or ( t1.lower() in easy_words)):
            print(token)
            res+=1
    return res
df['not_easy_words'] = df['docs'].apply( lambda x: f_not_easy_words(nlp(x)) )/df['ws']
df.plot(x= 'not_easy_words', y ='difficulty',style = 'o')

#compute avergae word length

def isLetter (input):
    for x in range (ord('a'), ord('z')+1):
        if (input==x):
            return True
    for x in range (ord('A'), ord('Z')+1):
        if (input==x):
            return True
    return False

def countLetters (doc):
    ltrCount=0
    for word in doc:
        for char in word:
            if (isLetter (ord(char))==True):
                ltrCount+=1
    print (ltrCount)
    return ltrCount

df['ttl_Chars'] = df['docs'].apply( lambda x: countLetters(x))
df['avg_wd_length'] = df['ttl_Chars']/df['ws']
df.plot(x= 'avg_wd_length', y ='difficulty',style = 'o')

df.to_csv( "updatedFeatures.csv", columns= [col1 for col1 in df.columns if col1 != 'docs']  )
