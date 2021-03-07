# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 20:29:44 2021

@author: SVW_E
"""

#数据加载
import pandas as pd
df=pd.read_csv('car_complain.csv')
#数据处理
df=df.drop('problem',axis=1).join(df.problem.str.get_dummies(','))
#数据清洗
def f(x):
    x=x.replace('一汽-大众','一汽大众')
    return x
df['brand']=df['brand'].apply(f) 
# print(df)
#按照品牌统计投诉总量    
result=df.groupby(['brand'])['id'].agg(['count'])
result=result.sort_values('count',ascending=False)
# print('各品牌投诉数量为')
# print(result)
# #按照品牌统计所有投诉分类的数量
# tags=df.columns[7:]
# print(tags)
# result2=df.groupby(['brand'])[tags].agg(['sum'])
# print(result2)
# #将投诉总数与各投诉分类数量结合在一起，形成一张大的表格
# result2=result.merge(result2,left_index=True, right_index=True, how='left')
# print(result2)
# #将表格索引正常化显示
# result2.reset_index(inplace=True)
# print(result2)
# result2.to_csv('./result.csv')
# #按照count,从大到小进行排序
# result2=result2.sort_values('count',ascending=False)
# print(result2)
# #查询某一内容的投诉量，并按照某一类型投诉量进行排序
# query=('A11','sum')
# print(result2.sort_values(query,ascending=False))
# 车型抱怨排序
# result3=df.groupby(['car_model'])['id'].agg(['count'])
# result3=result3.sort_values('count',ascending=False)
# print('各车型投诉数量为')
# print(result3)
# 品牌车型抱怨数量统计
result4=df.groupby(['brand','car_model'])['id'].agg(['count'])
print(result4)
# 计算各车型品牌数量
result5=result4.groupby(['brand'])['count'].agg(['count'])
print(result5)
result6=result.merge(result5,left_index=True, right_index=True, how='left')
result6.columns=['Brand_Complain_Number','Car_Model_Number']
print(result6)
result6['average']=result6['Brand_Complain_Number']/result6['Car_Model_Number']
result6=result6.sort_values('average',ascending=False)
print('各品牌平均车型投诉从多到少为')
print(result6)




