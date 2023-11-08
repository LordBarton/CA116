#!/usr/bin/env python3

s = input()
while s != "end":
    s = input()
    i = 0
    while i < len(s) and s[i] != ",":
        i += 1
    if s[i - 4:i] == "City":
        print(s[:i])
