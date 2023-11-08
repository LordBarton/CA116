#!/usr/bin/env python3

s = input()
L = len(s)
i = 0
t = ""

while i < L:
    if s[i] == " ":
        i += 1
    else:
        t += s[i]
        i += 1
print(t)
