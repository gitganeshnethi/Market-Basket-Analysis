# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 12:33:41 2019

@author: Administrator
"""
!pip install apyori
import pandas as pd
import numpy as np
from apyori import apriori
data = pd.read_csv('D:\\ML-Class\\Data Sets\\Apriori\\store_data.csv',header=None)
data.head()
li = []
'''
li_main = []
for i,rows in data.iterrows():
    for j in range(len(rows)):
        if rows[j] is not 'nan':
            li.append(rows[j])
    li_main.append(li)
'''
# each row is created as list and all lists(rows) are put in a single list
for i,rows in data.iterrows():
    x =rows.unique()
    x = filter(lambda v: v==v,x)
    li.append(list(x))
len(li[0])  

#model building
association_rules = apriori(li,min_support = 0.005,
                             min_confidence = 0.2, min_lift = 3,
                             min_length = 2)
rules = list(association_rules)

len(rules)
#f = rules[0]
#f[2][0][0]
df = pd.DataFrame()
for i in rules:
    a = i
    
    curr_row = {'Base_item':a[2][0][0],
                'Add_item':a[2][0][1],
                'Confidence':a[2][0][2],
                'lift':a[2][0][3]}
    df = df.append(curr_row,ignore_index=True)
type(df.Add_item[0])




 



