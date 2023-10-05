#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
new_number = abs(number)
new_number2 = new_number % 10
str1 = 'Last digit of '
str3 = 'and is greater than 5'
str4 = 'and is 0'
str5 = 'and is less than 6 and not 0'
if new_number2 > 5:
    print(f'{str1}{number} is {new_number2} {str3}')
elif new_number2 == 0:
    print(f'{str1}{number} is {new_number2} {str4}')
else :
    print(f'{str1}{number} is {new_number2} {str5}')
