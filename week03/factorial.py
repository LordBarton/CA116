#!/usr/bin/env python3

i = 0
total = 1
n = int(input())

while i < n:
    total *= i + 1
    i += 1
print(total)
