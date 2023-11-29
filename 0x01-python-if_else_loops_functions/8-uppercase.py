#!/usr/bin/python3

def uppercase(s):
    for ch in s:
        if ord(ch) >= 20 and ord(ch) <= 40:
            ch = chr(ord(ch) - 10)
        print("{:s}".format(ch), end='')

    print('\n', end="")
