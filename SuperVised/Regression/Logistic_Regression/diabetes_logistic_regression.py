# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 14:54:11 2023

@author: yusuf
"""


# logistic regression

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression ## logistic regression library
from sklearn.model_selection import train_test_split   ## train test
from sklearn.preprocessing import StandardScaler   ## for scaling
from sklearn.metrics import confusion_matrix   ## for model performance
from sklearn.metrics import accuracy_score    ## for accuracy


data = pd.read_csv("diabetes.csv")
print(data.head())

## outcome = 1 diabet / seker hastası
## outcome = 0 saglıklı

print(data.columns)  # print columns name
## 'Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
# 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome'

print(data.isnull().sum())  # no null data
print(data.info())
print(data.describe())
print(data.shape)
print(data.ndim)


## plotting

sick = data[data.Outcome == 1]  ## dataframe of sick people
healthy = data[data.Outcome == 0]  ## dataframe of healty people


## we can plot according glucose
 
plt.scatter(healthy.Age, healthy.Glucose, color = "g", label = "healthy", alpha = 0.4)
plt.scatter(sick.Age, sick.Glucose, color = "r", label = "diabet", alpha = 0.4)
plt.title("diabet according to age and glucose")
plt.xlabel("Age")
plt.ylabel("Glucose")
plt.legend()
plt.show()

## we can plot according pregnancies
 
plt.scatter(healthy.Age, healthy.Pregnancies, color = "purple", label = "healthy", alpha = 0.4)
plt.scatter(sick.Age, sick.Pregnancies, color = "yellow", label = "diabet", alpha = 0.4)
plt.title("diabet according to age and pregrancies")
plt.xlabel("Age")
plt.ylabel("pregrancies")
plt.legend()
plt.show()


## seperate the x and y

x_df = data.iloc[:,:-1] ## dataframe
print(x_df.head())

y_df = data.iloc[:,-1:]
print(y_df.head())

x_array = x_df.values
y_array = y_df.values 

## train and test

x_train, x_test, y_train, y_test = train_test_split(x_array, y_array, test_size = 0.3, random_state = 0)        


## scale

scale = StandardScaler()
x_train = scale.fit_transform(x_train)
x_test = scale.fit_transform(x_test)

print(x_train[:,:])  ## we can see the scale 


## logistic regression

model = LogisticRegression()  # random_state = 0
model.fit(x_train, y_train)


## prediction

y_pred = model.predict(x_test)
print(y_pred)


## evaluation matrix

conf_matrix = confusion_matrix(y_test, y_pred)
print(f"conf Matrix : \n{conf_matrix}")
#True Positive + True Negative = 136 + 42 
#False Positive + False Negative = 32 + 21


## accuracy

acc_score = accuracy_score(y_test, y_pred)
print(f"accuracy score : \n{acc_score}")  ## 0.77


## predict

test = model.predict([[6, 148, 72, 36, 0, 33.6, 0.627, 50]]) ## print 1 so correct
print(test)
