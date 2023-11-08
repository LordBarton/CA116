#!/usr/bin/env python3

s = input()
i = 0
L = len(s)
t = ""
while i < L:
    t += s[L - i - 1]
    i += 1
print(t)
