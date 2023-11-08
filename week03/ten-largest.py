#!/usr/bin/env python3

i = 0
nb = int(input())

while i < 9:
    n = int(input())
    if n > nb:
        nb = n
        i += 1
    else:
        i += 1
print(nb)
