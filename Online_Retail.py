# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 14:45:01 2019

@author: Administrator
"""

import pandas as pd
import numpy as np
from apyori import apriori
data = pd.read_excel('D:\\ML-Class\\Data Sets\\Apriori\\Online Retail.xlsx')
data.head()

data1=data[data['Country']=='France']
data1.shape
main_data = data1.iloc[:,[0,2]]

#u = main_data['InvoiceNo'].unique()

li = []
for i in main_data['InvoiceNo'].unique():
    l = list(main_data[(main_data['InvoiceNo'] == i)]['Description'])
    li.append(l)
            
#model building
association_rules = apriori(li,min_support = 0.05,
                             min_confidence = 0.2, min_lift = 3,
                             min_length = 3)
rules = list(association_rules)
len(rules)
rules[1]
df = pd.DataFrame()
for i in rules:
    a = i
    
    curr_row = {'Base_item':a[2][0][0],
                'Add_item':a[2][0][1],
                'Confidence':a[2][0][2],
                'lift':a[2][0][3]}
    df = df.append(curr_row,ignore_index=True)
df.head(20)