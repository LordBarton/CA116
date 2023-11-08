#!/usr/bin/env python3

s = input()
i = 0
a = ""
while s[i] != ".":
    a += s[i]
    i += 1
print(a)
print(s[i + 1:])
