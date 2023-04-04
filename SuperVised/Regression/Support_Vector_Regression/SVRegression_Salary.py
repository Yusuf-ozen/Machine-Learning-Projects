# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 17:18:54 2023

@author: yusuf
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler  ## scale
from sklearn.svm import SVR  ## support vector regression library



data = pd.read_csv("svr_salary.csv")
print(data)

## seperate x and y

x_df = data.iloc[:, 1 : 2]
y_df = data.iloc[:, -1:]


## plot

plt.scatter(x_df, y_df, color = "blue")
plt.title("Eğitim Seviyesi ve Maas")
plt.xlabel("Eğitim")
plt.ylabel("Maaş")
plt.legend()
plt.show()

## Feature Scaling
x_array = x_df.values
y_array = y_df.values

"""
scale = StandardScaler()
x_array = scale.fit_transform(x_array)
y_array = scale.fit_transform(y_array)
"""
## SVR

model = SVR(kernel = "rbf")  ## polynomial or gaussian type
model.fit(x_array, y_array)

## prediction
"""
#y_pred = scale.inverse_transform((model.predict(scale.transform(np.array([[6.5]])))))
y_pred = scale.inverse_transform(model.predict(scale.transform(np.array([[6.5]]))))
"""
y_pred = model.predict([[6.5]])
print(y_pred)

## plot after prediction

## plt.scatter(x_array, model.predict(x_array), color = "green")
plt.scatter(x_array, y_array, color = 'red')
plt.plot(x_array, model.predict(x_array), color = 'green')
plt.title("Eğitim Seviyesi ve Maas")
plt.xlabel("Eğitim")
plt.ylabel("Maaş")
plt.legend()
plt.show()














