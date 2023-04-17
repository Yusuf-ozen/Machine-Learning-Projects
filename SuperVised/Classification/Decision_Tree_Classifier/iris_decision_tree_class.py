# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 12:23:31 2023

@author: yusuf
"""


import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report


dataset = datasets.load_iris()

x = dataset.data
y = dataset.target


## scale

scale = StandardScaler()
x = scale.fit_transform(x)

## test train

x_train, x_test, y_train, y_true = train_test_split(x, y, test_size = 0.3, random_state = 0)            

## decision tree model

model = tree.DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

## score
cr = confusion_matrix(y_true, y_pred)
acc = accuracy_score(y_true, y_pred) * 100
re = classification_report(y_true, y_pred)


print(f"Accuracy : {acc}\nConfusion matrix : \n{cr}\nClassification Report : \n{re}")

