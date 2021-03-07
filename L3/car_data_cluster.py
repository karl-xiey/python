# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 10:03:04 2021

@author: SVW_E
"""
from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd
import numpy as np

#数据加载
data=pd.read_csv('car_data.csv',encoding='gbk')
print(data)
train_x=data[['人均GDP','城镇人口比重','交通工具消费价格指数','百户拥有汽车量']]
print(train_x)
#规范化到[0,1]空间
min_max_scaler=preprocessing.MinMaxScaler()
train_x=min_max_scaler.fit_transform(train_x)
pd.DataFrame(train_x).to_csv('temp.csv',index=False)
print(train_x)

#使用KMeans聚类
kmeans=KMeans(n_clusters=3)
predict_y=kmeans.fit_predict(train_x)
print(predict_y)
#合并聚类结果，并跟原来数据合并
result=pd.concat((data,pd.DataFrame(predict_y)),axis=1)
result.rename({0:u'聚类结果'},axis=1,inplace=True)
print(result)

#将结果导入到CSV文件中
result.to_csv('car_data_cluster_result.csv',index=False)

#K-Means手肘法：统计不同K取值的误差平方和
import matplotlib.pyplot as plt
sse=[]
for k in range(1,11):
    kmeans=KMeans(n_clusters=k)
    kmeans.fit(train_x)
    #计算intertia簇内误差平方和
    sse.append(kmeans.inertia_)
x=range(1,11)
plt.xlabel('K')
plt.ylabel('SSE')
plt.plot(x,sse,'.-')
plt.show

#使用层次聚类可视化
from scipy.cluster.hierarchy import dendrogram, ward
from sklearn.cluster import KMeans,AgglomerativeClustering
model=AgglomerativeClustering(linkage='ward',n_clusters=3)
#fit+predict
y=model.fit_predict(train_x)
print(y)
linkage_matrix=ward(train_x)
dendrogram(linkage_matrix)
plt.show()





