# -*- coding: utf-8 -*-
'''
Created on 2018��1��30��

@author: czera
'''
bonus1 = 100000*0.1
bonus2 = 100000*0.075
bonus3 = 200000*0.05
bonus4 = 200000*0.03
bonus5 = 400000*0.015

i=int(input('input:\n'))
if i<=100000:
    bonus = i*0.1
elif i<=200000:
    bonus = bonus1+(i-100000)*0.075
elif i<=400000:
    bonus = bonus1+bonus2+(i-200000)*0.05
elif i<=600000:
    bonus = bonus1+bonus2+bonus3+(i-400000)*0.03
elif i<=1000000:
    bonus = bonus1+bonus2+bonus3+bonus4+(i-600000)*0.015
else:
    bonus = bonus1+bonus2+bonus3+bonus4+bonus5+(i-1000000)*0.01
print('bonus=',bonus)