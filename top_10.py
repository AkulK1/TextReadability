# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 20:49:24 2020

@author: Bryant_Xia
"""
from wordfreq import word_frequency
from PyDictionary import PyDictionary
import spacy
nlp = spacy.load("en_core_web_sm")

dictionary=PyDictionary()

class word ():
    def __init__(self, txt, freq):
        self.txt = txt
        self.freq = freq

doc=nlp("""In ordinary language we describe by the word “planning” the complex of interrelated decisions about the allocation of our available resources. All economic activity is in this sense planning; and in any society in which many people collaborate, this planning, whoever does it, will in some measure have to be based on knowledge which, in the first instance, is not given to the planner but to somebody else, which somehow will have to be conveyed to the planner. The various ways in which the knowledge on which people base their plans is communicated to them is the crucial problem for any theory explaining the economic process, and the problem of what is the best way of utilizing knowledge initially dispersed among all the people is at least one of the main problems of economic policy—or of designing an efficient economic system.""")

diff_words=[]
all_words=[]

def top10 (doc):
    for token in doc:
        frq=word_frequency(token, 'en')
        temp=word (token, frq)
        all_words.append (temp)

top10(doc)
all_words.sort(key=lambda x: x.freq, reverse=False)

for x in range (10):
    diff_words.append (all_words[x])
    print (diff_words[x].txt)
    print (dictionary.meaning(str(diff_words[x].txt)))
    print ()


       
        
