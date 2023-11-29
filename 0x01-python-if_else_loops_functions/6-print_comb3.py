#!/usr/bin/python3

for first_digit in range(0,9):
    for j in range(i + 1, 10):
         print("{:d}{:d}".format(first_digit, second_digit), end=',
         ' if second_digit < 9 else '\n')
