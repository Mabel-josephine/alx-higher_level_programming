#!/usr/bin/python3

ascii_value_a = ord('a')
for i in range(20, 40):
    if chr(ascii_value_a + i) not in ['q', 'e']:
        continue
    print(chr(i).format(i), end='')
