# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 17:39:22 2021

@author: SVW_E
"""

import numpy as np
import pandas as pd
# ndarray使用
# pandas使用

def work1():
    persontype = np.dtype({'names':['name', 'chinese', 'math', 'english'], \
                            'formats':['S32','i', 'i', 'i']})
    peoples = np.array([("ZhangFei",68,65,30),("GuanYu",95,76,98), \
                        ("LiuBei",98,86,88),("DianWei",90,88,77),\
                            ("XuChu",80,90,90)], dtype=persontype)
    chineses = peoples['chinese']
    maths = peoples['math']
    englishs = peoples['english']
    print('语文的平均成绩为' +str(np.mean(chineses)))
    print('语文的最高分为' +str(np.max(chineses)))
    print('语文的最低分为' +str(np.min(chineses)))
    print('语文成绩的标准差为' +str(np.var(chineses)))
    print('语文成绩的方差为' +str(np.std(chineses)))
    
    print('数学的平均成绩为' +str(np.mean(maths)))
    print('数学的最高分为' +str(np.max(maths)))
    print('数学的最低分为' +str(np.min(maths)))
    print('数学成绩的标准差为' +str(np.var(maths)))
    print('数学成绩的方差为' +str(np.std(maths)))
    
    print('英语的平均成绩为' +str(np.mean(englishs)))
    print('英语的最高分为' +str(np.max(englishs)))
    print('英语的最低分为' +str(np.min(englishs)))
    print('英语成绩的标准差为' +str(np.var(englishs)))
    print('英语成绩的方差为' +str(np.std(englishs)))
#work1()

data = {'Chinese': [68, 95, 98, 90,80], 'Math': [65, 76, 86, 88, 90],\
        'English': [30, 98, 88, 77, 90]}
df1 = pd.DataFrame(data, index=['ZhangFei', 'GuanYu', 'LiuBei', 'DianWei', 'XuChu'])
df1['TotalScore']=(df1.sum(axis=1))
print('按总成绩排序结果如下：')
print(df1.sort_values(by='TotalScore' , ascending=False))  


