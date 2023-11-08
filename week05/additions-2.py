#!/usr/bin/env python3

s = input()
a = []
i = 0
total = 0
while i < len(s):
    j = i
    while i < len(s) and s[i] != "+":
        i += 1
    total += int(s[j:i])
    i += 1
print(total)
