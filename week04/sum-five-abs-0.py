#!/usr/bin/env python3

i = 0
total = 0

n = int(input())
while n != 0:
    if n < 0:
        n *= -1
    total += n
    n = int(input())
    i += 1
print(total)
