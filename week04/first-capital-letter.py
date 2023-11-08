#!/usr/bin/env python3

s = input()
L = len(s)
i = 0
t = ""

while i < L:
    if ord(s[i]) >= 65 and ord(s[i]) <= 90:
        t += chr(i)
    i += 1
print(ord(t[0]))
