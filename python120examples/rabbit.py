# -*- coding: utf-8 -*-
n=int(input('input the month: '))
if n%2 ==0:
    a=int((n-2)/2)
else:
    a=int((n-1)/2)
p1 = 1
p2 = 1
for i in range(a):
    p1 += p2
    p2 += p1
if n%2 == 0:
    print(p2)
else:
    print(p1)

    
