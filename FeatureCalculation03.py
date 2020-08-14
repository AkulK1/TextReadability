# -*- coding: utf-8 -*-

import pandas as pd
import spacy
from spacy_syllables import SpacySyllables

nlp = spacy.load("en_core_web_sm")
syllables = SpacySyllables(nlp)
nlp.add_pipe(syllables, after="tagger")

df = pd.read_csv( "Data03.csv" , index_col = 0)

def plot_graph( feat ):
    df.plot( x=feat, y='difficulty', style='o')

df['flesch_score'] = 206.835 - 1.015*df['ws_per_sents'] -84.6*df['syl_per_word']
plot_graph('flesch_score')

df['ari_score'] = 4.71*df['avg_wd_length']+0.5*df['ws_per_sents']
plot_graph('ari_score')

