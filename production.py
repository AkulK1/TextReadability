# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 22:15:44 2020

@author: Bryant_Xia
"""
import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error as MAE
from sklearn.model_selection import train_test_split, cross_val_score
import numpy as np


df = pd.read_csv( "cleaned.csv" )
predictors =['syl_per_word', 'ws_per_sents', 'monosyls',  'flesch_score', 'ari_score', 'dale_score', 'smog','gunning_fog', 'cli', 'linsear', 'det', 'sconj', 'avg_verb_length']
# predictors2 =['syl_per_word', 'ws_per_sents', 'monosyls',  'flesch_score', 'ari_score', 'dale_score', 'smog','gunning_fog', 'cli', 'linsear', 'det', 'sconj', 'avg_verb_length', 'sci_info']

# Xu = df[predictors2]
# yu = df['difficulty']

df[predictors] = StandardScaler().fit_transform( df[predictors] )

predictors.append( 'sci_info' )

X = df[predictors]
y = df['difficulty']


print( "Model      ", "  Accuracy", "  Adjancency" , "     MAE")

def testit( model, name ):
    
    print( '{:11}'.format(name) , end = ' '  )
    acc = 0
    ttl_mae = 0
    adj = 0
    for x in range(50):
        X_train, X_test, y_train, y_test =train_test_split (X, y, test_size=.3, random_state=x)
        model.fit( X_train, y_train )
        ttl_mae +=MAE(y_test, model.predict(X_test).round())
        temp = 0
        temp2 = 0
        temp3 = 0
        for i,j in zip(model.predict(X_test).round(), y_test):
            temp2+=1
            if (i==j):
                temp3+=1
            if abs( i-j) <= 1:
                temp+=1
        temp /= temp2
        temp3/=temp2
        adj+=temp
        acc+=temp3
    print(  '{:10.5f}'.format(acc/50),  '{:10.5f}'.format(adj/50), '{:10.5f}'.format(ttl_mae/50) )


from mord import LogisticAT

# for a in range(130, 160 ):
    
#     model_ordinal = LogisticAT(alpha=a/10000)
#     testit( model_ordinal, 'Ordinal '+  str(a/10000) )
model_ordinal2 = LogisticAT( alpha = .014 )
testit( model_ordinal2, "Ordinal LR")

#pickle the trained model

model_ordinal = LogisticAT( alpha = .014 )
X_train2, X_test2, y_train2, y_test2 =train_test_split (X, y, test_size=.3, random_state=23)
model_ordinal.fit( X, y )
print (MAE(y_test2, model_ordinal.predict(X_test2).round()))

temp = 0
temp2 = 0
temp3 = 0

compare=model_ordinal.predict(X_test2)

for i,j in zip(model_ordinal.predict(X_test2).round(), y_test2):
     temp2+=1
     if (i==j):
         temp3+=1
     if abs(i-j) <= 1:
         temp+=1
         
temp/=temp2
temp3/=temp2

print (temp3)
print (temp)

import pickle
pickl = {'model': model_ordinal}
pickle.dump( pickl, open( 'full_model' + ".p", "wb" ) )

file_name = "full_model.p"
with open(file_name, 'rb') as pickled:
    data = pickle.load(pickled)
    model = data['model']

print (list(X_test2.iloc[0,:])) ## prints all the predictors in X_test index 0
print (model.predict(np.array(list(X_test2.iloc[0,:])).reshape(1,-1))[0])

#pickled model works as intended; spits out the same predictions as train test split for the first (0th row) in X_test


# def testitunscaled( model, name ):
    
#     print( '{:11}'.format(name) , end = ' '  )
#     acc = 0
#     ttl_mae = 0
#     adj = 0
#     for x in range(50):
#         X_train, X_test, y_train, y_test =train_test_split (Xu, yu, test_size=.3, random_state=x)
#         model.fit( X_train, y_train )
#         ttl_mae +=MAE(y_test, model.predict(X_test).round())
#         temp = 0
#         temp2 = 0
#         temp3 = 0
#         for i,j in zip(model.predict(X_test).round(), y_test):
#             temp2+=1
#             if (i==j):
#                 temp3+=1
#             if abs( i-j) <= 1:
#                 temp+=1
#         temp /= temp2
#         temp3/=temp2
#         adj+=temp
#         acc+=temp3
#     print(  '{:10.5f}'.format(acc/50),  '{:10.5f}'.format(adj/50), '{:10.5f}'.format(ttl_mae/50) )
    
# model_unscaled = LogisticAT( alpha = .014 )
# testitunscaled( model_ordinal2, "Ordinal U")

# import pickle
# pickl = {'model': model_unscaled}
# pickle.dump( pickl, open( 'final' + ".p", "wb" ) )

# file_name = "final.p"
# with open(file_name, 'rb') as pickled:
#     data = pickle.load(pickled)
#     model = data['model']
# print (list(Xu.iloc[0,:]))
