# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#TextProBarV1
import time
scale = 10
print("-----start-----")
for i in range (scale + 1):
    a = '*' * i
    b = '.' * (scale - 1)
    c = (i / scale) * 100
    print("{:^3.0f}%[{}->{}]".format(c, a, b))
    time.sleep(0.1)
print("-----end-----")