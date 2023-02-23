# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 19:46:24 2021

@author: IXYTY
"""
#Calculate p.a.V1
money = 10000.00
year = 30
rate = 0.07
 
for y in range(year):
    money = money*rate + money
    print('第%d年结束时，本利合计：%.2f' % (y+1,money))
    print("")

