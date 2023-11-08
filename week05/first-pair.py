#!/usr/bin/env python3

s = input()
i = 0
j = 1

while i < len(s) and j < len(s) and s[i] != s[j]:
    i += 1
    j += 1
if i < len(s) and j < len(s):
    print(s[i:j + 1])
