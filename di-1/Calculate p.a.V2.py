# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 23:04:34 2021

@author: IXYTY
"""
#Calculate p.a.V2

s = 10000
x = 0
v=0

 
for i in range(31):
#    p = (a+(a*(i+1))/(i+1)

    x = (s)*(1.07**i)
    v += x
    t = v-(s*i)-s

    print("投资满{}年时存入前，账户余额{:.2f}元".format(i,v-s))
    print("投资满{}年时存入后，账户余额{:.2f}元".format(i,v))
    print("投资当满{}年时的利息为{:.2f}元".format(i,t))
    print("--------------------------------------")

print("--------------------------------------")
print("投资{}年后，账户余额{:.2f}元".format(i,v))
print("投资满{}年的利息为{:.2f}元".format(i,v-(s*i)))
print("投资结束时，账户余额为{:.2f}元".format(v-(s*i)+(s*30)-s))