# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 18:28:08 2023

@author: yusuf
"""

### libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression  ## multiple lineer
from sklearn.preprocessing import PolynomialFeatures  ## polynomial
from sklearn.metrics import mean_absolute_error



data = pd.read_csv("deliverytime.txt")
print(data.head(10))
print(data.columns)
print(data.info())  ## we have no null data
print(data.isnull().sum()) ## we have 0 null data in all columns

## we should calculate the  distance between restaurant and delivery locations using haversine formula    
earth_radius = 6371  ## km

## we should convert to degrees to radians 
def radians(degrees):
    radian = degrees * (np.pi / 180)
    return radian


def haversine(R_latitude, R_longitude, D_latitude, D_longitude):
    latitude_distance = radians(D_latitude - R_latitude)
    longitude_distance = radians(D_longitude - R_longitude)
    
    a = np.sin(latitude_distance / 2) ** 2
    b = np.cos(radians(R_latitude))
    c = np.cos(radians(D_latitude))
    d = np.sin(longitude_distance / 2) ** 2
    
    k = a + b * c * d
    m = 2 * np.arctan2(np.sqrt(k), np.sqrt(1 - k))
    
    return earth_radius * m

## create an empty column
data["distance"] = np.nan

## fill the column 
for i in range(len(data)):
    data.loc[i, "distance"] = haversine(data.loc[i, "Restaurant_latitude"], data.loc[i, "Restaurant_longitude"],
                                        data.loc[i, "Delivery_location_latitude"], data.loc[i, "Delivery_location_longitude"])       

print("----------------------------------------------")
print(data.head())

    
    
## array
"""
x1 = np.array(data[["Delivery_person_Age", 
                   "Delivery_person_Ratings", 
                   "distance"]])
"""

print("---------------------------------------------")
x2 = data.iloc[:, 2:4]  ## person_age ve person_ratings column
x3 = data.iloc[:, -1:]  ## distance column

## x2 = data.iloc[:, 3:5]  ## dataframe
## x2 = data.iloc[:, 3:5].values    ## array
## x2 = data.iloc[:, :5].values          ## array
## x3 = data.iloc[:, -1:].values       ## array
## x4 = data.iloc[:, 2].values      ## array

x = pd.concat([x2, x3], axis = 1).values ## connect x2 and x3 dataframe.


## y = np.array(data[["Time_taken(min)"]])  ## array
y = data.iloc[:, -2:-1].values


## train test
x_train, x_test, y_train, y_test =  train_test_split(x, y, test_size = 0.1, random_state = 42)

## we can use multiple lineer regresssion and polynomial lineer regression and LSTM neural network.
## lineer regression

lineer = LinearRegression()

lineer.fit(x_train, y_train)

predict = lineer.predict(x_test)
print(f"\npredict : {predict} ")


## calculate error
error = mean_absolute_error(y_test, predict)  ## true, prediction
print(f"error : {error}")


print("--------------------------------error")
print(np.mean(np.absolute(predict - y_test), axis=0))

###

print('Variance score: %.2f' % lineer.score(x_test, y_test))



"""
## polynomial regression
## x = x.reshape(-1, 1)  ## array

### 2 degree polynomial
poly = PolynomialFeatures(degree = 2)

x_poly = poly.fit_transform(x_train)

lineer2 = LinearRegression()
lineer2.fit(x_poly, y_train)



x_poly.predict(x_test)
lineer = LinearRegression()
lineer.fit(x_poly, y)

## predict with lineer regression
lin_predict = lineer2.predict(x_test)

## predict with polynomial regression
poly_predict = lineer2.predict(x_poly)
"""















