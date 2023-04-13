# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 16:25:37 2023

@author: yusuf
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, accuracy_score


data = pd.read_csv("reklam1.csv")
print(data.head())

print(data.info())
print(data.describe())
print(data.columns)
## ['KullaniciID', 'Cinsiyet', 'Yas', 'TahminiMaas', 'SatinAldiMi']

satin_aldi = data[data.SatinAldiMi == 1]
satin_almadi = data[data.SatinAldiMi == 0]

## yas ve maasa gore

plt.scatter(satin_aldi.Yas, satin_aldi.TahminiMaas, color = "red", label = "Satin aldi", alpha = 0.4)
plt.scatter(satin_almadi.Yas, satin_almadi.TahminiMaas, color = "blue", label = "Satin almadi", alpha = 0.4)
plt.xlabel("Yas")
plt.ylabel("Maas")
plt.grid(True)
plt.legend()
plt.show()

## cinsiyet ve maas

plt.scatter(satin_aldi.Cinsiyet, satin_aldi.TahminiMaas, color = "green", label = "Satin aldi", alpha = 0.4)
plt.scatter(satin_almadi.Cinsiyet, satin_almadi.TahminiMaas, color = "black", label = "Satin almadi", alpha = 0.4)
plt.xlabel("Cinsiyet")
plt.ylabel("Maas")
plt.grid(True)
plt.legend()
plt.show()

## X and Y

x = data[["Yas", "TahminiMaas"]]  ## df
y = data[["SatinAldiMi"]]  ## df

## train and test

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.30, random_state = 0)


## scale
scale = StandardScaler()
x_train = scale.fit_transform(x_train)
x_test = scale.fit_transform(x_test)
print(x_train[:10, :])

## SVM model
model = SVC(kernel = "rbf", random_state = 0)
## ‘linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’
## default = "rbf

model.fit(x_train, y_train)

## prediction

y_pred = model.predict(x_test)
print(y_pred[:10])   ## one dimension

## confusion matrix and accuracy

cr = confusion_matrix(y_test, y_pred)
print("confusion matrix : \n", cr)
## TN + TP = 75 + 28, FN + FP = 13 + 4

acc = accuracy_score(y_test, y_pred)
print("Accuracy Score : \n", acc)  ## 0.858  for linear, 0.85 for poly, 0.9 for rbf,
## 0.75 for sigmoid,  Precomputed matrix must be a square matrix. Input is a 280x2 matrix.
## rbf best result for this data
##score = model.score(x_test, y_test)



liste = []
    
for j in range(0,100):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = j)
    model2 = SVC(kernel = "rbf", random_state = j)
    model2.fit(x_train, y_train)
    score = model2.score(x_test, y_test) * 100
    #print(f"for random_state {j} :  score : {new_model.score(x_test, y_test) * 100}")
    liste.append(score)


print("--------------------------------------------------------")       
print(f"Best random_state value : {liste.index(max(liste)) + 1} and best score value : {max(liste)}")

## for this dataset random_state = 0 is best value

