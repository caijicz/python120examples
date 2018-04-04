import sys
for i in range(8):
    for j in range(8):
        if(i + j) % 2 == 0:
            sys.stdout.write(chr(19))
            sys.stdout.write(chr(19))
        else:
            sys.stdout.write(' ')
    print ('')