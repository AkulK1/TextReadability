from flask import Flask, request
import json
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

@app.route('/predict', methods=['POST'])

def predict():
    # stub input features
    # parse input features from request
    request_json = request.get_json()
    x = request_json['input']
    x_in = np.array(x).reshape(1, -1)
    # load model
    model = load_models()
    prediction = str(model.predict(x_in)[0])
    response = json.dumps({'response': prediction})
    return response, 200

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
    req_text = request.get_json()['input']
    feature_list = []
    
    
    #calculating features
    #features are ['syl_per_word', 'ws_per_sents', 'monosyls',  'flesch_score', 'ari_score', 'dale_score', 'smog','gunning_fog', 'cli', 'linsear', 'det', 'sconj', 'avg_verb_length']
    nlp = spacy.load("en_core_web_sm")
    syllables = SpacySyllables(nlp)
    nlp.add_pipe(syllables, after="tagger")
    
    doc = nlp(req_text)
    
    #syl_per_word
    ws =0
    syls =0
    for token in doc:
        if token._.syllables_count != None:
            ws+=1
            syls+=token._.syllables_count
    feature_list.append(syls/ws )
    
    #ws_per_sents    
    sentenceCount = len(list(doc.sents))
    wordCount = req_text.split()
    feature_list.append( wordCount/sentenceCount )
    
    #monosyls
    count_mono  = 0
    wss = 0
    for token in doc:
        syl1 = token._.syllables_count
        if  syl1 != None:
            wss+=1
            if syl1 == 1:
                count_mono+=1
    feature_list.append( count_mono/wss )
    
    #flesch_score
    #df['flesch_score'] = 206.835 - 1.015*df['ws_per_sents'] -84.6*df['syl_per_word']
    fkscore = 206.835 - 1.015*feature_list[1] - 84.6*feature_list[0]
    feature_list.append( fkscore )
    
    #ari_score
    ltrCount=0
    for word in req_text:
        for char in word:
            if (isLetter(ord(char))==True):
                ltrCount+=1
    avg_wd_len = ltrCount/wordCount
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
            
    percent_easy = res/wordCount
    feature_list.append( 0.1579*percent_easy*100 + 0.0496*feature_list[1] )

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
    
    feature_list.append(0.4(wordCount/sentenceCount+percent_easy))
 
    #'cli'
    cli = 0.0588*100*avg_wd_len-0.296*(sentenceCount/wordCount*100)-15.8
    feature_list.append(cli)
    
    #'linsear'
    linsear = (polysyls*300 +(1-polysyls)*100)/(sentenceCount/wordCount*100)
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
    feature_list.append(det)
    
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
    x_in =  StandardScaler().fit_transform( x_in )
    # load model
    model = load_models()
    prediction = str(model.predict(x_in)[0])
    
    response = json.dumps({'response': prediction})
    return response, 200


if __name__ == '__main__':
    app.run(debug=True)
 
