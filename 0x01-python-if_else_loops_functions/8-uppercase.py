#!/usr/bin/python3
def uppercase(str):
        """Prints a string in uppercase."""
        for me in str:
            if ord(me) >= 97 and ord(me) <= 122:
                me = chr(ord(me) - 32)
                print(f'{me}', end='')
