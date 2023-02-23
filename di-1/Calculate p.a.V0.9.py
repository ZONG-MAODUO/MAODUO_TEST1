# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 19:22:41 2021

@author: IXYTY
"""
#Calculate p.a.V0.9
a = 10000
b = 0.07

for i in range(31):
    c = a * ((1 + b)**i)
    print("整存{}年的收益是:{:.3f}".format(i,c-10000))
