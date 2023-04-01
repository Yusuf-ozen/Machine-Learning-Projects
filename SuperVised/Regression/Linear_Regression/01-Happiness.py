# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 16:12:54 2023

@author: yusuf
"""
### Linear Regression 1


### Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt   ## plotting
from scipy import stats  ## plot graph and line
from sklearn.linear_model import LinearRegression  ## linear regression 
from sklearn import metrics ## Accuracy classification score.




### data
data = pd.read_csv("income.data.csv")
print(data.head())

## check null data
print(data.isnull().sum())

## information about data
print(data.info())
print(data.shape)   ## (498,3)
print((data.describe()))  ## count, mean ...
  
## seperate independent and dependent variables
x = data.iloc[:, 1:2].values
x_graph = data["income"]  ## we use x_values like series so we can plot line
print(x.shape)
#print(x)

y = data.iloc[:,-1:].values
y_graph = data["happiness"]   ## series
## y_new = data[["happiness"]].values  ## dataframe 
print(y.shape)
#print(y)

## plotting
plt.scatter(x_graph, y_graph)
plt.show()

## line
#slope, intercept, r, p, se = stats.linregress(x_graph, y_graph)

"""
def function_X(x):
    return slope * x + intercept

my_model = list(map(function_X, x))
plt.scatter(x, y)
plt.plot(x, my_model)
plt.show()
"""

## plotting with line
res = stats.linregress(x_graph, y_graph)
print(f"R-squared: {res.rvalue**2:.6f}")
plt.plot(x_graph, y_graph, 'o', label='original data')
plt.plot(x_graph, res.intercept + res.slope*x_graph, 'r', label='fitted line')
plt.legend()
plt.show()

## create a model and fit
model = LinearRegression()
model.fit(x, y)

## r-square
r_sq = model.score(x, y)
print(f"coefficient of determination: {r_sq}")

## prediction
prediction = model.predict([[4.96]])  ## 4.96 income 
print(prediction)
print("\n------------------------------------------\n")

for i in range(10):
    print(f"income {i} : {x[i]}")
    print(f"happiness {i} : {y[i]}")
    print(f"predict {i} : {model.predict([x[i]])}")
    print("") ## for the space
    
## also you can check
## it has a dimensiol problem
"""
x_new = data["income"]
y_new = data["happiness"]

happines_pred = model.predict(x_new)
compare = pd.DataFrame({'real values': y_new, 'Prediction Values': happines_pred})
"""
## mean squared error value
happines_pred = model.predict(x)
print('Mean Squared Error:', metrics.mean_squared_error(y, happines_pred))

