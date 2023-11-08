#!/usr/bin/env python3

s = input()
i = 0
while i < len(s):
    j = i
    while i < len(s) and s[i] != ",":
        i += 1
    if i <= len(s):
        print(s[j:i])
    i += 1
