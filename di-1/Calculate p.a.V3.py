# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 19:49:01 2021

@author: IXYTY
"""
#Calculate p.a.V3
p = float(input("请输入您希望投资的本金!"))
a = float(input("请输入您的利率!"))
n = 0
result = p
while result<2*p:
    result = result*(1+a)
    n += 1
print("{}年后可以翻倍".format(n))