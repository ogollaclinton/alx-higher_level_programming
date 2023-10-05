#!/usr/bin/python3

for me1 in range(10):
    for me2 in range(me1 + 1, 10):
        if me1 == 8 and me2 == 9:
            print(f'{me1}{me2}')
        else:
            print("{:me1}{:me2}".format(me1. me2))
