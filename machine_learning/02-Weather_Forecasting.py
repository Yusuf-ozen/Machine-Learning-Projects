# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 18:25:05 2023

@author: yusuf
"""

### in this projects I used multiple linear regression. Also my score is very low.

### libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sbn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error



train_data = pd.read_csv("DailyDelhiClimateTrain.csv")
print(train_data)

test_data = pd.read_csv("DailyDelhiClimateTest.csv")
print(test_data)

### we should combine train and test
train_data = pd.concat([train_data, test_data], axis = 0)
print("-------------------DATA")
print(train_data)


### statistics of data

print("---------------------------------\DESCRIBEn")
print(train_data.describe())

### information about the columns

print("----------------------------INFO\n")
print(train_data.info()) 

### plot

##figure = px.line(train_data, x = "date", y = "meantemp", title = 'Mean Temperature', color= "date")        
##figure.show()

## you can also check null 
print(train_data.isnull().any())


## rename train_data with data
data = train_data

## plot the columns

data.plot(subplots=True, figsize=(25,20))

## plot 1 year

## data['2014':'2015'].resample('D').fillna(method='pad').plot(subplots=True, figsize=(25,20))
## data.hist(bins=10,figsize=(15,15))

## print(data.columns)

y = data.iloc[:, 1:2]
x = data.drop(["meantemp", "date"], axis = 1)

## training

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 2)
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)
print(y_train.head(10))

### multiple linear regression

model = LinearRegression()
model.fit(x_train, y_train)

predict = model.predict(x_test)

## error 
error = mean_absolute_error(y_test, predict)
print(error)

print("--------------------------------error")
print(np.mean(np.absolute(predict - y_test), axis=0))

###

print('Variance score: %.2f' % model.score(x_test, y_test))

###
"""
for i in range(len(predict)):
    predict[i] = round(predict[i], 2)

pd.DataFrame({"Real " : y_test, "predict " : predict, "difference" : y_test - predict})
"""




























