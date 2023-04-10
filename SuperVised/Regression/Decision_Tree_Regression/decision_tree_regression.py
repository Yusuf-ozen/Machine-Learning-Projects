# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 19:02:47 2023

@author: yusuf
"""

## libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
# import export_graphviz
from sklearn.tree import export_graphviz 
  


data = pd.read_csv("PozisyonSeviyeMaas.csv")
print(data.head())

print(data.columns)  
print(data.isnull().sum())  # no null data
print(data.info())
print(data.describe())
print(data.shape)
print(data.ndim)


## X and Y

x = data.iloc[:, 1:2]   ## seviye(df)
y = data.iloc[:, -1:]  ## maas(df)
x = x.values
y = y.values
## plot

plt.scatter(x, y, s = 100, color = "red", edgecolors = "g")
plt.title("Seviye ve Maaş")
plt.xlabel("Seviye")
plt.ylabel("Maaş")
plt.grid(True)
plt.show()

## train model

model = DecisionTreeRegressor(random_state = 0)
model.fit(x, y)

## prediction

y_pred = model.predict([[7.5]])
print(y_pred)


for i in range(0,9):
    print(f"Y_true {i+1} : {y[i]}  Y_pred {i+1} : {model.predict([[i]])}")
    

#### plot with decision

X_grid = np.arange(min(x), max(x), 0.01)
  
X_grid = X_grid.reshape((len(X_grid), 1)) 
  
# scatter plot for original data
plt.scatter(x, y, color = 'red')
  
# plot predicted data
plt.plot(X_grid, model.predict(X_grid), color = 'blue') 
  
# specify title
plt.title('seviye ve maas') 
  
# specify X axis label
plt.xlabel('seviye')
  
# specify Y axis label
plt.ylabel('maas')
  
# show the plot
plt.show()
    

export_graphviz(model, out_file ='tree.dot', feature_names =['maas']) 


