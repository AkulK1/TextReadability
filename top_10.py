# -*- coding: utf-8 -*-

"""
Created on Tue Sep  8 20:49:24 2020
@author: Bryant_Xia
"""

from wordfreq import zipf_frequency
from PyDictionary import PyDictionary
from wordfreq import tokenize
import spacy
from spacy_syllables import SpacySyllables
nlp = spacy.load("en_core_web_sm")
syllables = SpacySyllables(nlp)


import pandas as pd

dictionary=PyDictionary()

raw_text = """In ordinary language we describe by the word “planning” the complex of interrelated decisions about the allocation of our available resources. All economic activity is in this sense planning; and in any society in which many people collaborate, this planning, whoever does it, will in some measure have to be based on knowledge which, in the first instance, is not given to the planner but to somebody else, which somehow will have to be conveyed to the planner. The various ways in which the knowledge on which people base their plans is communicated to them is the crucial problem for any theory explaining the economic process, and the problem of what is the best way of utilizing knowledge initially dispersed among all the people is at least one of the main problems of economic policy—or of designing an efficient economic system."""
doc = tokenize(raw_text, 'en' )
unique_words= set()

def unique (doc):
    for token in doc:
        unique_words.add (token)
        
unique (doc)

doc=list (unique_words)

diff_words=[]
all_words=[]
freqs=[]
lens=[]
syl_count=[]

def attributes (doc):
    for token in doc:
        frq=zipf_frequency(token, 'en')
        all_words.append (token)
        freqs.append (frq)
        lens.append (len(token))
        syl_count.append(token._.syllables_count)

attributes (doc)

df=pd.DataFrame ()

df['words'] = all_words
df['freq'] = freqs
df['lens'] = lens
df['syl_count'] = syl_count

df['freq_z'] = -(df.freq - df.freq.mean())/df.freq.std(ddof=0)
df['lens_z'] = (df.lens - df.lens.mean())/df.lens.std(ddof=0)
df['syl_count_z'] = (df.syl_count - df.syl_count.mean())/df.syl_count.std(ddof=0)
df['tabulate']=df['freq_z']+df['lens_z']+df['syl_count_z']
df=df.sort_values('tabulate', ascending=False)
index=0

for wd in df['words']:
    if (index<10):
        diff_words.append (wd)
        print (diff_words[index])
        print (dictionary.meaning(diff_words[index]))
        index=index+1
    else:
        break
       
