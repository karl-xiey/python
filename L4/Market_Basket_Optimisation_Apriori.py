# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 10:52:19 2021

@author: SVW_E
"""


import pandas as pd
pd.set_option('max_columns',None)
#数据加载
dataset=pd.read_csv('./Market_Basket_Optimisation.csv',header=None)
print(dataset)
print(dataset.shape) #数据shape大小
transactions=[]
#按照行数进行遍历
for i in range(0,dataset.shape[0]):
    #按列数进行遍历
    temp=[] #记录一行的Transection
    for j in range(0,dataset.shape[1]):
        if str(dataset.values[i,j]) !='nan':
            temp.append(dataset.values[i,j])
    # print(temp)
    transactions.append(temp)    

from efficient_apriori import apriori
itemsets,rules=apriori(transactions, min_support=0.02,min_confidence=0.3)
print('频繁项集',itemsets)
print('关联规则',rules)


