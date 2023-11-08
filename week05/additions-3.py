#!/usr/bin/env python3

total = 0
while total != 1000:
    s = input()
    i = 0
    j = i
    while i < len(s) and s[i] != ".":
        i += 1
    total += int(s[j:i])
    i += 1
print(total)
