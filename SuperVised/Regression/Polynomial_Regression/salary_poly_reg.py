# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 23:35:07 2023

@author: yusuf
"""

### Polynomial Regression

## Libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures ## polynomial


data = pd.read_csv("maaslar.csv")
print(data)

## independent value
x = data.iloc[:, 1:2].values   ## eğitim seviyesi
print(x)


## dependent value
y = data.iloc[:, -1:].values  ## maas
print(y)


### scatter plot
plt.scatter(x, y, s = 100, c = "green", edgecolors = "red")
plt.title("eğitim seviyesi ve maas")
plt.xlabel("eğitim seviyesi")
plt.ylabel("maas")
#plt.grid(True)  
plt.legend()
plt.show()

### fit model linear regression
lr = LinearRegression()  ## model object
lr.fit(x, y)  # train data


## plot line lineer regression

plt.scatter(x, y, color = 'red') 
plt.plot(x, lr.predict(x), color = 'blue') # plotting the linear regression line
plt.title('eğitim ve maaş (Linear Regression)') 
plt.xlabel('eğitim') 
plt.ylabel('maas')
plt.show() 


### training polynomial regression model

poly_reg = PolynomialFeatures(degree = 5)  ## 4 and 5 is good
x_poly = poly_reg.fit_transform(x)   ## transform the features to the polynomial


lr2 = LinearRegression()  ## new linear regression object
lr2.fit(x_poly, y)  ## yeni x ve y'miz

y_new_plot = lr2.predict(x_poly)


### plot with polynomial regression

plt.scatter(x, y, color = "blue")
plt.plot(x, y_new_plot, color = "red")
plt.title("eğitim ve maas (Polynomial Regression)")
plt.xlabel("eğitim")
plt.ylabel("maas")
plt.show()


"""
## deneme
for i in range(10):
    deneme_poly = PolynomialFeatures(degree = i)
    deneme_x = deneme_poly.fit_transform(x)
    lr_deneme = LinearRegression()
    lr_deneme.fit(deneme_x, y)
    deneme_plot = lr_deneme.predict(deneme_x)
    
    plt.scatter(x, y, color = "yellow")
    plt.plot(x, y_new_plot, color = "red")
    plt.title("eğitim ve maas (Polynomial Regression)")
    plt.xlabel("eğitim")
    plt.ylabel("maas")
    plt.show()
  """  
  
## compare linear regression and polynomial regression for this dataset

dneme = lr.predict([[4]])
print(dneme)

po_deneme = lr2.predict(poly_reg.fit_transform([[4]]))
print(po_deneme)

for i in range(1,10):
    print(f"original value {i} : {y[i]}")
    model_linear = lr.predict([[i]])
    print(f"lineer model i {i} : {model_linear}")
    model_polynomial = lr2.predict(poly_reg.fit_transform([[i]]))
    print(f"polynomial model {i}: {model_polynomial}")
    print("")
    