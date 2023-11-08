#!/usr/bin/env python3

s = input()
i = 0
t = ""

while i < len(s):
    if ord(s[i]) >= 97 and ord(s[i]) <= 122:
        ts = ord(s[i]) - 32
        t += chr(ts)
        i += 1
    else:
        t += s[i]
        i += 1
print(t)
