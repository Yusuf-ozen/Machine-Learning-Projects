# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 21:26:14 2023

@author: yusuf
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("train.csv")
print(data.head(10))


print("\n----------------------")
print(data.info())

## gereksiz sütunları atalım.

data = data.iloc[:, 5:]
data = data.drop(["Occupation", "Type_of_Loan"], axis = 1)
print("\n-----------------------")
print(data.head(10))
data = data[["Credit_Utilization_Ratio", "Credit_Score"]]
print("\n------------------------")
print(data)

## label encoding

from sklearn.preprocessing import LabelEncoder
label = LabelEncoder()

score = data.iloc[:, -1:].values  ## -1'e kadarkileri al, sonrasını alma.
print("------------------------------ labelsiz")
print(score)


score = label.fit_transform(score)  ## score 
score = score.reshape(-1, 1)
print("--------------------------- labelli")
print(score)

## one hot encoder
from sklearn.preprocessing import OneHotEncoder
one = OneHotEncoder()
score = one.fit_transform(score).toarray()
print("------------------------ onehot")
print(score)
##
## score = score.reshape(-1, 1)
print("------------------")
print(type(score))

data["Credit_Score"] = score

## good = 0, poor = 1, standard = 2

## x ve y'yi olusturalım.

x = data["Credit_Utilization_Ratio"].values
y = data["Credit_Score"].values

##

x = x.reshape(-1, 1)

## train test

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state= 1)        

## linear regression

from sklearn.linear_model import LinearRegression

lineer = LinearRegression()
lineer.fit(x_train, y_train)
prediction = lineer.predict(x_test)
print("-------------------------------------------")
print(prediction)

## plot

plt.plot(x, y, color = "g")
plt.show()

## 
print("----------------\nTAHMIN")
print(lineer.predict([[35]]))  ## 0.18 yani good











