import numpy as np
n = int(input('please write the number of datasets you want: '))
for i in range(n):
    bianchang = input('please insert the length of the bricks and length of the wall: ' ).split()
    bianchang_list = list(map(int,bianchang))
    if (bianchang_list[0]%2 ==1 ) and (bianchang_list[1]%2 == 1):
        shape = []
        for j in range(bianchang[0]):
            temp = []
            for k in range(bianchang[0]):
                temp.append(input().split())
        print(shape)
        
    

