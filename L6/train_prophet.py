# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 12:26:25 2021

@author: SVW_E
"""
import pandas as pd
from fbprophet import Prophet
#数据加载
train=pd.read_csv('./train.csv')
# print(train)
#转换位pandas中的数据格式
train['Datetime']=pd.to_datetime(train['Datetime'])
# print(train)
#将datetime作为index,丢掉没用的ID和多余的Datetime
train.index=train['Datetime']
train.drop(['ID','Datetime'],axis=1,inplace=True)
# print(train)
#按照天进行采样
daily_train=train.resample('D').sum()
# print(daily_train)
#设置模型保留字
daily_train['ds']=daily_train.index
daily_train['y']=daily_train['Count']
daily_train.drop(['Count'],axis=1,inplace=True)
# print(daily_train)

#创建Prophet模型
m=Prophet(yearly_seasonality=True,seasonality_prior_scale=0.1)
m.fit(daily_train)
#预测未来7个月，213天
future = m.make_future_dataframe(periods=213)
forecast=m.predict(future)
# print(forecast)
m.plot(forecast)


