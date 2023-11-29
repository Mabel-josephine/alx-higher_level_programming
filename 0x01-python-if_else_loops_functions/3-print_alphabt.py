#!/usr/bin/python3

for char in map(chr, range(ord('a'), ord('z') + 1)):
    print(f"{char}", end="" if char != 'z' else "\n")
