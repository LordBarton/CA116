#!/usr/bin/env python3

i = 0
sp = int(input())

while i < 9:
    n = int(input())
    if n < sp and n > 0:
        sp = n
    i += 1

print(sp)
