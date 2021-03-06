

#input the file name in text_title
text_title = 'b002_LittleBear.txt'

#input 1 for info and 0 for fiction
number_for_info = 0

#feature_list is what would be calculated by flask and feature_list_actual is what was used to train model




import pickle
import numpy as np
import spacy
from spacy_syllables import SpacySyllables

import pandas as pd


def load_models():
    file_name = "models/model_scaler.p"
    with open(file_name, 'rb') as pickled:
       data = pickle.load(pickled)
       model = data['model']
    return model

def load_scaler():
    file_name = "models/model_scaler.p"
    with open(file_name, 'rb') as pickled:
       data = pickle.load(pickled)
       sc = data['scaler']
    return sc

def isLetter (input):
    for x in range (ord('a'), ord('z')+1):
        if (input==x):
            return True
    for x in range (ord('A'), ord('Z')+1):
        if (input==x):
            return True
    return False

def countLetters (token):
    ltrCount=0
    for char in token:
        if (isLetter (ord(char))==True):
            ltrCount+=1
    return ltrCount


df = pd.read_csv( "../DataWithTexts.csv" , index_col = 0)

req_json = {}
temp_series = df.loc[df['text'] == text_title]['docs']


temp_list = temp_series.tolist()


req_json['input'] = temp_list[0]
req_json['info'] = number_for_info



req_text = req_json['input']

feature_list = []


#calculating features
#features are ['syl_per_word', 'ws_per_sents', 'monosyls',  'flesch_score', 'ari_score', 'dale_score', 'smog','gunning_fog', 'cli', 'linsear', 'det', 'sconj', 'avg_verb_length']
nlp = spacy.load("en_core_web_sm")
syllables = SpacySyllables(nlp)
nlp.add_pipe(syllables, after="tagger")

doc = nlp(req_text)

#syl_per_word
ws=0
syls=0
for token in doc:
    if token._.syllables_count != None:
        ws+=1
        syls+=token._.syllables_count
feature_list.append(syls/ws)

#ws_per_sents    
sentenceCount = len(list(doc.sents))
ws = len(req_text.split())
temp=  ws/sentenceCount
feature_list.append(temp)

#monosyls
count_mono  = 0
wss = 0
for token in doc:
    syl1 = token._.syllables_count
    if  syl1 != None:
        wss+=1
        if syl1 == 1:
            count_mono+=1
temp=count_mono/wss
feature_list.append(temp)

#flesch_score
#df['flesch_score'] = 206.835 - 1.015*df['ws_per_sents'] -84.6*df['syl_per_word']
fkscore = 206.835 - 1.015*feature_list[1] - 84.6*feature_list[0]
feature_list.append(fkscore)

#ari_score
ltrCount=0
for word in req_text:
    for char in word:
        if (isLetter(ord(char))==True):
            ltrCount+=1
avg_wd_len = ltrCount/ws
feature_list.append( 4.71*avg_wd_len + 0.5*feature_list[1] )

#dale_score
ff = open('EasyList.txt', 'r')
easy_words = [i.lower() for i in ff.read().split()]
res = 0
for token in doc:
    t1 =  token.lemma_
    t1 = t1.lower()
    if (token._.syllables_count != None) and not ( (token.text.lower() in easy_words) or ( t1.lower() in easy_words)):
        res+=1
percent_easy = res/ws
feature_list.append( 0.1579*percent_easy*100 + 0.0496*feature_list[1])

#smog
import math

poly  = 0

for token in doc:
    syl1 = token._.syllables_count
    if  syl1 != None and syl1 > 2:
        poly+=1
        
polysyls = poly/ws
smog=3+math.sqrt(polysyls)
feature_list.append(smog)

 
#'gunning_fog'

feature_list.append(0.4*(ws/sentenceCount+percent_easy))
 
#'cli'
cli = 0.0588*100*avg_wd_len-0.296*(sentenceCount/ws*100)-15.8
feature_list.append(cli)

#'linsear'
linsear = (polysyls*300 +(1-polysyls)*100)/(sentenceCount/ws*100)
if (linsear>20):
    linsear=linsear/2
else:
    linsear=linsear/2-1
feature_list.append(linsear)

#'det'
det=0
for token in doc:
    if (token.pos_=="DET"):
        det+=1;
det=det/sentenceCount
feature_list.append(det)

#'sconj'
sconj=0
for token in doc:
    if (token.pos_=="SCONJ"):
        sconj+=1;
sconj=sconj/sentenceCount
feature_list.append(sconj)

#'avg_verb_length'
vCount=0;
cCount=0;
for token in doc:
    if (token.pos_=="VERB"):
        vCount+=1;
        cCount+=countLetters (token.text)
avg_vb_length=0
if (cCount==0):
    avg_vb_length=0
else:
    avg_vb_length=cCount/vCount
feature_list.append(avg_vb_length)



#scaling data and getting model's prediction
x_in = np.array(feature_list).reshape(1, -1)
x_in =  load_scaler().transform( x_in )

#add info
x_in = np.append(x_in, [req_json['info']])

# load model
model = load_models()
prediction = str(model.predict(x_in)[0])
print( "difficulty:", prediction )

df2 = pd.read_csv( "../cleaned.csv" )
predictors =['syl_per_word', 'ws_per_sents', 'monosyls',  'flesch_score', 'ari_score', 'dale_score', 'smog','gunning_fog', 'cli', 'linsear', 'det', 'sconj', 'avg_verb_length']

feature_list_actual = (df2.loc[df2['titles']==text_title][predictors]).iloc[0].tolist()

print()
print( text_title )
print( "calculated by flask" )
print( feature_list )
print()
print( "actually used to train model")
print( feature_list_actual )
print()
print( "scaled" )
print( x_in )
