# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 22:40:19 2020

@author: kuangkuang
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import mean_absolute_error as MAE
df = pd.read_csv( "no_text.csv")

print (df.columns)

from sklearn.model_selection import train_test_split
predictors =['syl_per_word', 'ws_per_sents', 'not_easy_words', 'avg_wd_length', 'polysyls', 'monosyls', 'adj', 'verb', 'adp', 'adv', 'sconj', 'cconj', 'aux', 'det', 'avg_verb_length', 'avg_adj_length', 'avg_adv_length', 'flesch_score', 'ari_score', 'dale_score', 'smog','gunning_fog', 'cli', 'linsear']
X=df[predictors]
y=df['difficulty']

X_train, X_test, y_train, y_test =train_test_split (X, y, test_size=.4, random_state=1)

model = RandomForestRegressor (max_depth=None, random_state=1)
model.fit (X_train, y_train)
y_pred=model.predict (X_test)
y_pred_series = pd.Series(y_pred)
y_pred_series=y_pred_series.round ()
print (MAE (y_test, y_pred_series))

from sklearn.linear_model import LinearRegression, Lasso
from sklearn.model_selection import cross_val_score

lm = LinearRegression()
lm.fit(X_train, y_train)

np.mean(cross_val_score(lm,X_train,y_train, scoring = 'neg_mean_absolute_error', cv= 3))

# lasso regression  
#Ken Jee
lm_l = Lasso(alpha=.13)
lm_l.fit(X_train,y_train)
np.mean(cross_val_score(lm_l,X_train,y_train, scoring = 'neg_mean_absolute_error', cv= 3))
alpha = []
error = []

for i in range(1,30):
    alpha.append(i/1000)
    lml = Lasso(alpha=(i/1000))
    error.append(np.mean(cross_val_score(lml,X_train,y_train, scoring = 'neg_mean_absolute_error', cv= 3)))
    
plt.plot(alpha,error)
err = tuple(zip(alpha,error))

# gridsearch
#Ken Jee

from sklearn.model_selection import GridSearchCV
parameters = {'n_estimators':range(10,300,10), 'criterion':('mse','mae'), 'max_features':('auto','sqrt','log2')}

gs = GridSearchCV(model,parameters,scoring='neg_mean_absolute_error',cv=3)
gs.fit(X_train,y_train)

print (gs.best_score_)
print (gs.best_estimator_)
