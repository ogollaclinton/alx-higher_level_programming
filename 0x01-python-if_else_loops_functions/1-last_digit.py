#!/usr/bin/python3
import random
import math
num = random.randint(-10000, 10000)
last_dgt = abs(number) % 10
if num < 0:
    last_dgt = -last_d
    print(f"Last digit of {num} is {last_dgt}", end=" ")
if last_dgt > 5:
    print(f"Last digit of {num} is {last_dgt} and is greater than 5")
elif last_dgt == 0:
    print(f"Last digit of {num} is {last_dgt} and is 0")
else:
    print("and is less than 6 and not 0")
