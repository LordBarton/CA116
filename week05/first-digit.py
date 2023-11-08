#!/usr/bin/env python3

s = input()
i = 0

while i < len(s) and (ord(s[i]) < 48 or ord(s[i]) > 57):
    i += 1

if i < len(s):
    print(s[i], i)
