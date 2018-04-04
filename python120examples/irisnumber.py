for i in range(100,1000):
    q = i%10
    j = int(i/100)
    p = (int(i/10))%10
    if i == (pow(q,3)+pow(j, 3)+pow(p, 3)):
        print(i)

