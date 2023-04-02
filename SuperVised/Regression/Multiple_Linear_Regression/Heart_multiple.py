# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 10:52:26 2023

@author: yusuf
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split  ## test and train
from sklearn import metrics



data = pd.read_csv("heart.data.csv")  ## dataframe
print(data.head())

print(data.isnull().sum())  ## check data

print(data.info())  ## information and check data
print(data.shape)
print(data.ndim)   ## dimension
print(data.describe())  ## numeric values


## setting X and Y
x = data[["biking", "smoking"]]  ## dataframe
x_new = data.iloc[:, 1:3]

y = data["heart.disease"]  ## series
y_new = data.iloc[:,-1:]   ## dataframe


## plot

plt.scatter(x_new.biking, y_new, color = "g")
plt.scatter(x_new.smoking, y_new, color = "r")
plt.show()

"""
## plot >> did not work
plt.plot(x_new["biking"], y_new, 'o', label = "biking")
plt.plot(x_new["smoking"], y_new, 'o', label = "smoking")
plt.legend()
plt.show()
"""

## train and test

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 100)           
multiple_reg = LinearRegression()
multiple_reg.fit(x_train, y_train)


### model equations

print("Intercept : ", multiple_reg.intercept_)  # 14.92
print("Coefficients : ", list(zip(x, multiple_reg.coef_))) # biking : -0.2, smoking : 0.17


### prediction

y_pred =  multiple_reg.predict(x_test)

difference = pd.DataFrame({"Real Value : " : y_test, "Prediction Value" : y_pred})
print(difference.head(15))


## model evaluation

print(f"R squared : {multiple_reg.score(x, y) * 100}")

meanAbsoluteError = metrics.mean_absolute_error(y_test, y_pred)
print(f"Mean absolute error : {meanAbsoluteError}")

meanSquaredError = metrics.mean_squared_error(y_test, y_pred)
print(f"Mean squared error : {meanSquaredError}")

rootMeanSquaredError = np.sqrt(metrics.mean_squared_error(y_test, y_pred))
print(f"Root Mean squared : {rootMeanSquaredError}")

