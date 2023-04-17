# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 00:29:43 2023

@author: yusuf
"""
"""
In this part i used the apyori in : bilkav.com/makine-ogrenmesi-egitimi/ to use aprori
"""

import numpy as np
import pandas as pd
from apyori import apriori

data = pd.read_csv("sepet.csv", header = None) 

liste = []

for i in range(0, len(data)):
    liste.append([str(data.values[i, j]) for j in range(0, 20)])


rules = apriori(liste, min_support = 0.01, min_confidence = 0.2, min_lift = 3, min_length = 2)   

print(list(rules))
