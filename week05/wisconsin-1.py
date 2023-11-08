#!/usr/bin/env python3

s = input()
while s != "end":
    i = 0
    while i < len(s) and s[i] != "I":
        i += 1
    if i < len(s) and s[i - 1] == "W":
        print(s[0:i - 2])
    s = input()
