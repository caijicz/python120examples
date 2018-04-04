from math import sqrt
num = 0
leap = 0
for i in range(101,201):
    k = int(sqrt(i))
    for j in range(2,k+1):
        if i%j == 0:
            leap = 1
            break 
    if leap == 0:
        print(i)
        num += 1
    leap = 0
print('the total number of voxels is: %d' %num)
    
    
    