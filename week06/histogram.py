#!/usr/bin/env python3

b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
s = input()
while s != "end":
    i = 0
    while i < len(s):
        j = 0
        while int(s[i]) != j:
            j += 1
        if j < 10:
            b[j] += 1
        i += 1
    s = input()
i = 0
while i < 10:
    print(i, "*" * b[i])
    i += 1
