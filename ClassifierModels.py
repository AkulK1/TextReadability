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
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis



df = pd.read_csv( "cleaned.csv" )
#print( df.columns )

# corr_dict = {}
# for col1 in df.columns:
#     if df[col1].dtypes in ["int64", 'float64' ]:
#         corr_dict[col1] = df[col1].corr( df['difficulty'] )



# #print correlations in increasing order
# for k1,v1 in sorted(corr_dict.items(), key=lambda p:p[1]):
#     print(k1,v1)
# print('\n')

predictors =['syl_per_word', 'ws_per_sents', 'monosyls',  'flesch_score', 'ari_score', 'dale_score', 'smog','gunning_fog', 'cli', 'linsear']

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
        ttl_mae +=MAE(y_test, model.predict(X_test))
        temp = 0
        temp2 = 0
        temp3 = 0
        for i,j in zip(model.predict(X_test), y_test):
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

logreg = LogisticRegression( random_state = 10, max_iter = 400 )
testit( logreg, 'LogReg')

gnb = GaussianNB()
testit( gnb, 'GNB')

knn = KNeighborsClassifier( n_neighbors = 5)
testit( knn, 'KNN5' )


lda = LinearDiscriminantAnalysis()
testit( lda, "LDA")




lsvc = SVC( kernel  = 'linear', random_state=10 )
testit( lsvc, 'Linear SVC')

rbf_svc = SVC( kernel = 'rbf', random_state = 10 )
testit( rbf_svc, 'RBF SVC')



from sklearn.base import clone

#https://gist.github.com/M46F/c574f688715d5f7e4b65bce4b3ec5fdc
class OrdinalClassifier():
    
    def __init__(self, clf):
        self.clf = clf
        self.clfs = {}
    
    def fit(self, X, y):
        self.unique_class = np.sort(np.unique(y))
        if self.unique_class.shape[0] > 2:
            for i in range(self.unique_class.shape[0]-1):
                # for each k - 1 ordinal value we fit a binary classification problem
                binary_y = (y > self.unique_class[i]).astype(np.uint8)
                clf = clone(self.clf)
                clf.fit(X, binary_y)
                self.clfs[i] = clf
    
    def predict_proba(self, X):
        clfs_predict = {k:self.clfs[k].predict_proba(X) for k in self.clfs}
        predicted = []
        for i,y in enumerate(self.unique_class):
            if i == 0:
                # V1 = 1 - Pr(y > V1)
                predicted.append(1 - clfs_predict[i][:,1])
            elif i in clfs_predict:
                # Vi = Pr(y > Vi-1) - Pr(y > Vi)
                 predicted.append(clfs_predict[i-1][:,1] - clfs_predict[i][:,1])
            else:
                # Vk = Pr(y > Vk-1)
                predicted.append(clfs_predict[i-1][:,1])
                
        
        return np.vstack(predicted).T
    
    def predict(self, X):
        return np.argmax(self.predict_proba(X), axis=1)+1
    
    def test_parts( self, X , y):
        print(self.clf)
        for i, j in zip(self.clfs, range(self.unique_class.shape[0]-1)):
            print( self.clfs[i].score( X , (y > self.unique_class[j]).astype(np.uint8) ), self.unique_class[j] )
        print( ' ')


print( "\nOrdinal Models")

ordlogreg = OrdinalClassifier(LogisticRegression( random_state = 10, max_iter = 400 ))
testit( ordlogreg, 'LogReg')

# ordlogreg.predict( np.array(X_test.iloc[0]).reshape( 1, -1 ) )
# y_test.iloc[0]
# ordlogreg.test_parts( np.array(X_test.iloc[0]).reshape( 1, -1 ), np.array(y_test.iloc[0]).reshape( 1, -1 ) )

ordgnb = OrdinalClassifier(GaussianNB())
testit( ordgnb, 'GNB')

ordknn = OrdinalClassifier(KNeighborsClassifier( n_neighbors = 5))
testit( ordknn, 'KNN5' )



ordlda = OrdinalClassifier(LinearDiscriminantAnalysis())
testit( ordlda, "LDA")



ordlsvc = OrdinalClassifier(SVC( kernel  = 'linear', random_state=10, probability = True))
testit( ordlsvc, 'Linear SVC')

ordrbf_svc = OrdinalClassifier(SVC( kernel = 'rbf', random_state = 10, probability = True ))
testit( ordrbf_svc, 'RBF SVC')

print("\n")
from mord import LogisticAT

# for a in range(130, 160 ):
    
#     model_ordinal = LogisticAT(alpha=a/10000)
#     testit( model_ordinal, 'Ordinal '+  str(a/10000) )
model_ordinal = LogisticAT( alpha = .014 )
testit( model_ordinal, "Ordinal LR")

