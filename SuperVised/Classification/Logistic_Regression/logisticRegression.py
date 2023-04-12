# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 11:59:14 2023

@author: yusuf
"""

import numpy as  np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
#from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score


data = pd.read_csv("reklam.csv")
print(data.head())

print(data.columns)
## ['KullaniciID', 'Cinsiyet', 'Yas', 'TahminiMaas', 'SatinAldiMi']

print(data.isnull().sum())
print(data.info())

#print(data.describe)


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


## x and y

x = data.iloc[:, 2:4]   ## df
#y = data.iloc[:, 4]   ## series
y = data.iloc[:, 4:]    ## df

## test and train

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 0)

# feature scale
scale = StandardScaler()
x_train = scale.fit_transform(x_train)
x_test = scale.fit_transform(x_test)
print(x_train[1:10,:])  ## we can see the scale 


## model

model = LogisticRegression(random_state = 42)
model.fit(x_train, y_train)

## prediction
y_pred = model.predict(x_test)

## confusion matrix
cr = confusion_matrix(y_test, y_pred)
print(f"Confusion Matrix : \n{cr}")
## 72 + 30 = 102, 1 + 17 = 18
#True Positive + True Negative = 72 + 30
#False Positive + False Negative = 1 + 17

## accuracy
acc_score = accuracy_score(y_test, y_pred)
print(f"Accuracy Score : \n{acc_score}")   ##   traintestsplit(random_state = 42) >> 0.85
##   traintestsplit(random_state = 0) >> 0.89

## test
test = model.predict([[30, 5000]])  ## 30 yas ve 5000 maas
print(test)   ## 1

"""
from matplotlib.colors import ListedColormap
X_set, y_set = x_test, y_test
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
         np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, model.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('blue', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
     plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                 c = ListedColormap(('yellow', 'green'))(i), label = j)
plt.title('Lojistik Regresyon (Test seti)')
plt.xlabel('Yaş')
plt.ylabel('Maaş')
plt.legend()
plt.show()
"""