# -*- coding: utf-8 -*-
'''
Created on 2018��1��30��

@author: czera
'''
import math

for i in range(100000):
    x=int(math.sqrt(i+100))
    y=int(math.sqrt(i+268))
    if(x*x==i+100)and(y*y==i+268):
        print('\n%d\n',i)
    