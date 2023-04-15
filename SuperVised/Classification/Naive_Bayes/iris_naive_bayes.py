# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 13:19:38 2023

@author: yusuf
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB  ## BernoulliNB # MultinomialNB
from sklearn.metrics import confusion_matrix, accuracy_score


data = pd.read_csv("Iris.csv")
print(data.head())

print(data.columns)
## ['Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm',
## 'Species'
print(data.info())
print(data.describe())


## plot

#plt.plot(data.Id, data.SepalLengthCm, color = "blue")  >> iki şekilde de kullanılır.
plt.plot(data["Id"], data["SepalLengthCm"], "g-*")
plt.title("ID and Sepal length")
plt.xlabel("Id")
plt.ylabel("Sepal Length")
plt.grid(True)
plt.show()


plt.scatter(x = data["SepalLengthCm"], y = data["SepalWidthCm"], color = "red")
plt.grid(True)
plt.show()

"""

plot(kind ="scatter",
          x ='SepalLengthCm',
          y ='PetalLengthCm')
plt.grid()

"""

## X and Y

x = data.iloc[:, 1:5].values
y = data.iloc[:, -1:].values

## train test

x_train, x_test, y_train, y_true = train_test_split(x, y, test_size = 0.30, random_state = 0)
   
## model

model = GaussianNB()
model.fit(x_train, y_train.ravel())
"""
A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().
  y = column_or_1d(y, warn=True)
"""

## prediction

y_pred = model.predict(x_test)
# print(y_pred[1:10])

## confusion matrix and accuracy

cr = confusion_matrix(y_true, y_pred)
acc = accuracy_score(y_true, y_pred)
print(f"------------------------------\nconf_matrix : \n{cr}\nacc_score : {acc}")
"""
conf_matrix : 
[[16  0  0]
 [ 0 18  0]
 [ 0  0 11]]
acc_score : 1.0

"""
print(f"score : {model.score(x_test, y_true) * 100}")


