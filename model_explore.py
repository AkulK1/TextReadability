# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 22:40:19 2020

@author: kuangkuang
"""
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import mean_absolute_error as MAE
df = pd.read_csv( "no_text.csv")

print (df.columns)

from sklearn.model_selection import train_test_split
predictors =['syl_per_word', 'ws_per_sents', 'not_easy_words', 'avg_wd_length', 'polysyls', 'monosyls', 'modals_per_sent', 'adj', 'verb', 'adp', 'adv', 'sconj', 'cconj', 'aux', 'det', 'avg_verb_length', 'avg_adj_length', 'avg_adv_length', 'flesch_score', 'ari_score', 'dale_score', 'SMOG','gunning_fog', 'CLI']
X=df[predictors]
y=df['difficulty']

X_train, X_test, y_train, y_test =train_test_split (X, y, test_size=.4, random_state=1)

model = RandomForestRegressor (max_depth=5, random_state=1)
model.fit (X_train, y_train)
y_pred=model.predict (X_test)
y_pred_series = pd.Series(y_pred)
y_pred_series=y_pred_series.round ()
print (MAE (y_test, y_pred_series))
