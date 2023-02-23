# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 22:26:25 2021

@author: IXYTY
"""
#1*(1+0.07)^n-2>0求N
a = 1
for i in range(20):
    dayup = pow(1.07, i)
    print(dayup)
    a += 1
    print("a{}".format(a))
    if dayup > 2:
        print(i)

