#!/usr/bin/env python3

s = input()
i = 0
L = len(s)
t = "abcdefg"
p = ""

while i < L:
    j = 0
    while j < 7:
        if s[i] == t[j]:
            p += t[j]
        j += 1
    i += 1
print(p[0])
