#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
new_number = abs(number) % 10
if number < 0:
    new_number = -new_number
    print(f"Last digit of {number:d} is {digit:d} and is ", end="")
    if new_number > 5:
        print("greater than 5")
    elif new_number == 0:
        print("0")
    else:
        print("less than 6 and not 0")
