#!/usr/bin/env python3

s = input()
i = 0
L = len(s)
total = 0

while i < L:
    total += int(s[i])
    i += 1
print(total)
