#!/usr/bin/python3

d = 0
for i in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(i - d)), end="")
    d = 32 if d == 0 else 0
