#!/usr/bin/env python3

s = input()
L = len(s)

print(s[L - 1] + s[1:L - 1] + s[0])
