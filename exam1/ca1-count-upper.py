#!/usr/bin/env python3

s = input()
i = 0
total = 0

while i < len(s):
    if s[i] >= "A" and s[i] <= "Z":
        total += 1
    i += 1
print(total)
