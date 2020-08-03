# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 15:00:14 2020

@author: AE401
"""
b=int(input("體重: "))
h=int(input("身高:"))
h=h/100
bmi=b//float(h)**2
if bmi >=18.5:
    print('體重不足')
elif bmi >=24:
    print('正常')
elif bmi >=27:
    print('過重')
elif bmi >=30:
    print('輕度肥胖')
elif bmi >=35:
    print('中度肥胖')
else:
    print('重度肥胖')