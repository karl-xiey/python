# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 18:32:17 2021

@author: SVW_E
"""

import pandas as pd
#加载数据
result=pd.read_excel('./car_complain.xlsx')

#分析type的内容，拆分成年份，发动机，变速器（自动/手动），其他
def analyze(type):
    year, engine, transmission, other='','','',''
    engine_list=['1.2T','1.4T','1.5T','1.8T','2.0T','2.5T','2.8T','1.2L','1.4L',\
                 '1.5L','1.6L','1.8L','2.0L','2.4L','2.5L','200TSI','280TSI',\
                 '330TSI','380TSI']
    for i in type:
        if type.index(i)==0 and i[-1:]=='款':
           year=i[:-1]
           continue
        if i=="手动" or i=='自动':
           transmission=i
           continue
        if i in engine_list:
           engine=i
           continue
        other=other+' '+i
    return year, engine, transmission, other

#年份 type_year
result['type_year']=''
result['type_engine']=''
result['type_transmission']=''
result['type_other']=''
#分析type字段，拆分成多个字段
for i, row in result.iterrows():
     year, engine, transmission, other=analyze(row['type'].split(' '))
     result.loc[i, 'type_year']=year
     result.loc[i, 'type_engine']=engine
     result.loc[i, 'type_transmission']=transmission
     result.loc[i, 'type_other']=other
#删除列,axis=1代表列，有columns就不用写了
result=result.drop(columns=['type'],axis=1)
print(result)
result.to_excel('temp.xlsx',index=False)

     
     