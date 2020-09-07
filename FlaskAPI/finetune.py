# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 10:22:24 2020

@author: kuangkuang
"""

from flask import Flask, request
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
import spacy
from spacy_syllables import SpacySyllables

app = Flask(__name__)

def load_models():
    file_name = "models/full_model.p"
    with open(file_name, 'rb') as pickled:
       data = pickle.load(pickled)
       model = data['model']
    return model

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

@app.route( '/textpred', methods = ['POST'] )

def textpred():
    req_text = "Fourscore and seven years ago our fathers brought forth, on this continent, a new nation, conceived in liberty, and dedicated to the proposition that all men are created equal. Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived, and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting-place for those who here gave their lives, that that nation might live. It is altogether fitting and proper that we should do this. But, in a larger sense, we cannot dedicate, we cannot consecrate—we cannot hallow—this ground. The brave men, living and dead, who struggled here, have consecrated it far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us—that from these honored dead we take increased devotion to that cause for which they here gave the last full measure of devotion—that we here highly resolve that these dead shall not have died in vain—that this nation, under God, shall have a new birth of freedom, and that government of the people, by the people, for the people, shall not perish from the earth."
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
    temp=ws/sentenceCount
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
    ff = open('EasyWordList.txt', 'r')
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
    print(temp)
    if (linsear>20):
        print("HI")
        linsear=linsear/2
        print(linsear)
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
    
    #manually adding info text
    
    feature_list.append(1)
    #scaling data and getting model's prediction
    x_in = np.array(feature_list).reshape(1, -1)
    # load model
    model = load_models()
    prediction = str(model.predict(x_in)[0])
    print(prediction)
    print(feature_list)


textpred()
