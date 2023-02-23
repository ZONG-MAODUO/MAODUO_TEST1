# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 18:43:46 2021

@author: IXYTY
"""
#BMIV1
height, weight = eval(input("请输入身高（米）和体重\（公斤）[逗号隔开]:"))
bmi = weight / pow(height, 2)
print("BMI 数值为:{:.2f}".format(bmi))
who, nat = "", ""
if bmi < 18.5:
    who = "偏瘦", "偏瘦"
elif 24 <= bmi < 25:
    who = "正常", "正常"
elif 25 <= bmi < 28:
    who = "偏胖", "偏胖"
elif 28 <= bmi < 30:
    who = "偏胖", "肥胖"
else:
    who = "肥胖"
print("BMI指标为：国际'{0}'".format(who))