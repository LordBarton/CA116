#!/usr/bin/env python3

s = input()
i = 0
while s[i] != " ":
    i += 1
j = i + 1
while s[j] != " ":
    j += 1
g = j + 1
while s[g] != ",":
    g += 1
print(s[j + 1:g] + " " + s[i + 1:j] + s[g:] + " (" + s[0:i] + ")")
