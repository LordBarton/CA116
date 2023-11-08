#!/usr/bin/env python3

s = input()
total = 0
while s != "end":
    i = 0
    while i < len(s) and s[i] != "I":
        i += 1
    if i < len(s) and s[i - 1] == "W":
        total += 1
    s = input()
print(total)
