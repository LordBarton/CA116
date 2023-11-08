#!/usr/bin/env python3

i = 0
se = int(input())

while i < 9:
    n = int(input())
    if n < se and n % 2 == 0:
        se = n
    i += 1
print(se)
