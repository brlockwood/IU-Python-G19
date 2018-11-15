# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 20:52:15 2018
@author: Prema Satish Vuyyuri
IU Python G19 Group Final Project Phase 1
"""

import pandas as pd
import pylab as plt
import numpy as np
from collections import defaultdict, Counter

data = pd.read_csv("BreastCancerWisconsin.csv")

print(data.head())
data.A7.replace('?', np.NaN)
data['A7']= pd.to_numeric(data['A7'], errors = 'coerce')
pd.isnull(data).any()
data.isnull().sum()

data1 = data.fillna(data.mean())
pd.isnull(data1).any()
data1.describe()

print(data1.shape)
print(data1.index.shape)
len(data1.index)
len(data1.columns)

data1['Scn'].nunique()
data1['Scn'].size

data1.plot(kind='scatter', x='A2', y='A3', s=120, c='RGB')
plt.xlabel('A2 - Clump Thickness')
plt.ylabel('A3 - Uniformity of Cell Size')
plt.show()

histpltdata = data1.iloc[:, [1,2,3,4,5,6,7,8,9]]
print(histpltdata.head())
plt.hist(histpltdata, bins=9, range=[1,9], alpha=1)
plt.show()

#barchart
brdata = data1['CLASS'].value_counts()
print(brdata.head())
df=pd.DataFrame(brdata)
df.reset_index(inplace=True)
df
df=df.rename(columns={'index':'ClassID'})
def myfunc(cl):
    rt = 'Maligant'
    if cl == 2:
        rt = 'Benign'
    return rt
myfunc('2')
df['ClassName'] = df.apply(lambda row: myfunc(row.ClassID), axis=1)
df
plt.bar(x=df['ClassName'],height=df['CLASS'], color='green')
plt.xlabel('ClassName')
plt.ylabel('Counts')
plt.show()

#print(data)
data1.A10.plot(kind='line', color='green', label='Mitoses', linewidth=2, alpha=0.5, grid=False, linestyle='-')
#data1.CLASS.plot(kind='bar', color='red', label='Class', linewidth=2, alpha=0.5, grid=False, linestyle=':')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

data1.plot(kind='Scatter', x='A7', y='A8', alpha=0.7, color='blue', grid=True)
