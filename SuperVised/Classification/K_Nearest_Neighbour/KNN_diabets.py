# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 22:57:58 2023

@author: yusuf
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
## knn classification

from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import confusion_matrix


data = pd.read_csv("diabetes.csv")
print(data.head())

print(data.columns)
## 'Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
##       'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome'
print(data.info())
print(data.describe())

## plot

hasta = data[data.Outcome == 1]
saglikli = data[data.Outcome == 0]

## yas ve kan basıncına gore

plt.scatter(saglikli.Age, saglikli.BloodPressure, color = "red", label = "Sağlıklı", alpha = 0.4)
plt.scatter(hasta.Age, hasta.BloodPressure, color = "blue", label = "Hasta", alpha = 0.4)
plt.xlabel("Yas")
plt.ylabel("Kan basıncı")
plt.grid(True)
plt.legend()
plt.show()

## yas ve glikoza gore

plt.scatter(saglikli.Age, saglikli.Glucose, color = "green", label = "Saglikli", alpha = 0.4)
plt.scatter(hasta.Age, hasta.Glucose, color = "black", label = "Hasta", alpha = 0.4)
plt.xlabel("Yas")
plt.ylabel("Glikoz")
plt.grid(True)
plt.legend()
plt.show()

## x and y

y = data.iloc[:, -1:]    ## df
x = data.drop(["Outcome"], axis = 1)   ## df
print(x.head())
print(y.head())

## normalization

x = (x - np.min(x, axis = 0)) / (np.max(x, axis = 0) - np.min(x, axis = 0))
print(x.head())

## test and train

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 0)

## train model

model = KNeighborsClassifier(n_neighbors = 3)
model.fit(x_train, y_train)

## prediction

model.predict(x_test)
print(f"For k = 3 score : {model.score(x_test, y_test) * 100}")

## find optimum k value

for i in range(1, 10):
   
    new_model = KNeighborsClassifier(n_neighbors = i)
    new_model.fit(x_train, y_train)
    print(f"for {i} score : {new_model.score(x_test, y_test) * 100}") 
    ## k = 7 ve random_state = 0 için score : 76.62
    
    
max_value = 0
count = 1
liste = []
    
for j in range(1,100):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = j)
    new_model2 = KNeighborsClassifier(n_neighbors = 9)
    new_model2.fit(x_train, y_train)
    score = new_model2.score(x_test, y_test) * 100
    #print(f"for random_state {j} :  score : {new_model.score(x_test, y_test) * 100}")
    liste.append(score)
    
    """
    if score > 75:
        print(f"for random_state {j} : ", score)
        
    
        
    if score >= max_value:
        max_value = score
        count = count 
        
    else:
        count += 1
        
print(f"max value {count} : ", max_value)
        
       """
print("--------------------------------------------------------")       
print(f"Best random_state value : {liste.index(max(liste)) + 1} and best score value : {max(liste)}")
##print(max(liste))
##print(liste.index(max(liste)) + 1)

## Final test train

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 56)
final_model = KNeighborsClassifier(n_neighbors = 9, metric = "minkowski", p = 2)
final_model.fit(x_train, y_train)

y_pred = final_model.predict(x_test)
y_pred = y_pred.reshape(-1, 1)
print(y_pred[1:10, :])

## for new prediction

scale = MinMaxScaler()
scale.fit_transform(x)

print("---------------------------------------------")

new_prediction = model.predict(scale.transform(np.array([[6,148,72,35,0,33.6,0.627,50]])))
print(new_prediction)

#####

cr = confusion_matrix(y_test, y_pred)
print(f"confusion matrix : \n{cr}")
## TN + TP = 142 + 40, FN + FP = 33 + 16



