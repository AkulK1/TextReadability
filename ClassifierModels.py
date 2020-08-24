# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 19:23:40 2020

@author: kesar
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_absolute_error as MAE
from sklearn.metrics import mean_squared_error as MSE
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis



df = pd.read_csv( "cleaned.csv" )

predictors =['syl_per_word', 'ws_per_sents', 'monosyls',  'adj', 'verb', 'adp', 'adv', 'sconj', 'det', 'avg_verb_length', 'avg_adj_length', 'avg_adv_length',  'flesch_score', 'ari_score', 'dale_score', 'smog','gunning_fog', 'cli', 'linsear']

#predictors =['monosyls','adj', 'verb', 'adp', 'adv', 'sconj', 'det', 'flesch_score', 'ari_score', 'dale_score', 'smog','gunning_fog', 'cli', 'linsear']


df[predictors] = StandardScaler().fit_transform( df[predictors] )
predictors.append( 'sci_info' )

X = df[predictors]
y = df['difficulty']
X_train, X_test, y_train, y_test =train_test_split (X, y, test_size=.3, random_state= 1)


print( "Model      ", "  Accuracy", "  Adjancency" , "     MAE")

def testit( model, name ):
    acc = 0
    ttl_mae = 0
    adj = 0
    for x in range(50):
        X_train, X_test, y_train, y_test =train_test_split (X, y, test_size=.3, random_state=x)
        model.fit( X_train, y_train )
        acc+= model.score(X_test, y_test)
        ttl_mae +=MAE(y_test, model.predict(X_test))
        temp = 0
        temp2 = 0
        for i,j in zip(model.predict(X_test), y_test):
            temp2+=1
            if abs( i-j) <= 1:
                temp+=1
        temp /= temp2
        adj+=temp
    print( '{:11}'.format(name) , '{:10.3f}'.format(acc/50),  '{:10.3f}'.format(adj/50), '{:10.3f}'.format(ttl_mae/50) )

logreg = LogisticRegression( random_state = 10, max_iter = 400 )
testit( logreg, 'LogReg')

gnb = GaussianNB()
testit( gnb, 'GNB')

knn = KNeighborsClassifier( n_neighbors = 5)
testit( knn, 'KNN5' )

rf = RandomForestClassifier(random_state = 10 )
testit( rf, "RF" )

ada = AdaBoostClassifier( random_state = 10 )
testit( ada, "ADA")

lda = LinearDiscriminantAnalysis()
testit( lda, "LDA")

gp = GaussianProcessClassifier( random_state = 10)
testit(gp, "GP")


lsvc = SVC( kernel  = 'linear', random_state=10 )
testit( lsvc, 'Linear SVC')

rbf_svc = SVC( kernel = 'rbf', random_state = 10 )
testit( rbf_svc, 'RBF SVC')