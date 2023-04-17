# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 17:58:34 2023

@author: yusuf
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


data = pd.read_csv("reklamr.csv")
print(data.head())

## X and Y

x = data.iloc[:, 2:4] ##df
y = data.iloc[:, -1:]  ##df
X = data.iloc[:, 1:4].values  ## array
Y = data.iloc[:, -1:].values  ## array
print(x)
print(y)

## label encoding 

le = LabelEncoder()
cinsiyet = X[:, 0]
cinsiyet = le.fit_transform(cinsiyet)
print(cinsiyet)
print(cinsiyet.ndim)

#X[:, 0] = le.fit_transform(X[])
##cinsiyet = x.iloc[:,:1]  ##df

## One Hot Encoder

one = OneHotEncoder()
cinsiyet = cinsiyet.reshape(-1, 1)
cinsiyet = one.fit_transform(cinsiyet).toarray()
print(cinsiyet)

###### 

cinsiyet_df = pd.DataFrame(data = cinsiyet, index = range(400), columns=["k", "e"])

final_df = pd.concat([x,cinsiyet_df], axis = 1)
print(final_df)

## test train

x_train, x_test, y_train, y_true = train_test_split(final_df, Y, test_size = 0.3, random_state = 0)       

## scale

scale = StandardScaler()
x_train = scale.fit_transform(x_train)
x_test = scale.fit_transform(x_test)

## model

model = RandomForestClassifier(n_estimators = 10, criterion = "entropy", random_state = 0)
model.fit(x_train, y_train.ravel())   ## df has no ravel

## prediction

y_pred = model.predict(x_test)

## conf matrix, acc and classification report

acc = accuracy_score(y_true, y_pred) * 100
cr = confusion_matrix(y_true, y_pred)
re = classification_report(y_true, y_pred)


print(f"Accuracy : {acc}\nConfusion matrix : \n{cr}\nClassification Report : \n{re}")
print("-----------------------------------------------------------------------\nYukarıdakinde cinsiyeti encode işlemi uygulayarak kullandık.Altta kullanmayacagiz.")
print("------------------------------------------------------------------------")

## X and Y

x1 = data.iloc[:, 2:4].values ##df  >> yas, tahmini maas
y1 = data.iloc[:, -1:].values  ##df
print(x)
print(y)


## test train

x1_train, x1_test, y1_train, y1_true = train_test_split(x1, y1, test_size = 0.3, random_state = 0)       

## scale

scale1 = StandardScaler()
x1_train = scale1.fit_transform(x1_train)
x1_test = scale1.fit_transform(x1_test)

## model

model1 = RandomForestClassifier(n_estimators = 10, criterion = "entropy", random_state = 0)
model1.fit(x1_train, y1_train.ravel())   

## prediction

y1_pred = model1.predict(x1_test)

## conf matrix, acc and classification report

acc1 = accuracy_score(y1_true, y1_pred) * 100
cr1 = confusion_matrix(y1_true, y1_pred)
re1 = classification_report(y1_true, y1_pred)


print(f"Accuracy : {acc1}\nConfusion matrix : \n{cr1}\nClassification Report : \n{re1}")
print("--------------------------------------------------------------------")
print("Cinsiyetin çıkarılması sonucu değiştirmedi.(score = 90)")
print("---------------------------------------------------------------------")
