# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 21:55:16 2020

@author: kesar
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import RidgeCV

df = pd.read_csv( "cleaned.csv" )
print (df.columns)

predictors =['syl_per_word', 'ws_per_sents', 'not_easy_words', 'avg_wd_length', 'monosyls', 'adj', 'verb', 'adp', 'adv', 'sconj', 'cconj', 'aux', 'det', 'avg_verb_length', 'avg_adj_length', 'avg_adv_length',  'smog']
df[predictors] = StandardScaler().fit_transform( df[predictors] )
predictors.append( 'sci_info' )
X=df[predictors]
y=df['difficulty']
X_train, X_test, y_train, y_test =train_test_split (X, y, test_size=.3, random_state=2323)

ols = LinearRegression()
ols.fit( X_train, y_train )
print( 'mse: ', mean_squared_error(ols.predict(X_test).round(), y_test) )

#https://github.com/Q-shick/fundamentals_of_data_science/blob/master/mathematical%20_model/Ridge%20and%20Lasso.ipynb
ridge = Ridge(alpha=0)
ridge.fit( X_train, y_train)
ridge_train_pred = []
ridge_test_pred = []
alphas = np.arange(0, 200, 1)

for alpha in alphas:
    ridge = Ridge(alpha=alpha)
    ridge.fit(X_train, y_train)
    # prediction
    ridge_train_pred.append(ridge.predict(X_train))
    ridge_test_pred.append(ridge.predict(X_test))

lasso_reg = Lasso(alpha=1)
lasso_reg.fit(X_train, y_train)

lasso_train_pred = []
lasso_test_pred = []
alphas = np.arange(0.01, 8.01, 0.04)
for alpha in alphas:
    lasso_reg = Lasso(alpha=alpha)
    lasso_reg.fit(X_train, y_train)
    lasso_train_pred.append(lasso_reg.predict(X_train))
    lasso_test_pred.append(lasso_reg.predict(X_test))
    
ridge_mse_train = [mean_squared_error(y_train, p.round() ) for p in ridge_train_pred]
lasso_mse_train = [mean_squared_error(y_train, p.round() ) for p in lasso_train_pred]

ridge_mse_test = [mean_squared_error(y_test, p.round()) for p in ridge_test_pred]
lasso_mse_test = [mean_squared_error(y_test, p.round()) for p in lasso_test_pred]

fig, axes = plt.subplots(2, 2, figsize=(10, 10))
plt.rcParams['axes.grid'] = True

axes[0,0].plot(ridge_mse_train, 'b', ridge_mse_test, 'r')
axes[0,0].set_title("Ridge Regression MSE", fontsize=16)
axes[0,0].set_ylabel("MSE")
axes[0,1].plot(lasso_mse_train, 'b', lasso_mse_test, 'r')
axes[0,1].set_title("Lasso Regression MSE", fontsize=16)

param = {'alpha': np.arange(0.01, 10, 0.01)}

ridge_reg_grid = GridSearchCV(Ridge(), param )
ridge_reg_grid.fit(X_train, y_train)
ridge_grid_pred = ridge_reg_grid.predict(X_test)

print(ridge_reg_grid.best_estimator_)
print( 'ols mse: ', mean_squared_error(ols.predict(X_test).round(), y_test) )

print("gridsearch ridge MSE:", mean_squared_error(y_test, ridge_grid_pred.round()))



print( 'ols r2: ', r2_score(ols.predict(X_test).round(), y_test) )

print("gridsearch ridge r2:", r2_score(y_test, ridge_grid_pred.round()))