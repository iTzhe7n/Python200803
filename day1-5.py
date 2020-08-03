# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 14:29:11 2020

@author: AE401
"""

score = input('請輸入成績')
score = int(score)
if score >=0 and score <=100:
    
    if score >=90:
        print('A')
    elif score >=80:
        print('B')
    elif score >=70:
        print('C')
    elif score >=60:
        print('D')
    else:
        print('E')
else:
    print('錯誤')
    