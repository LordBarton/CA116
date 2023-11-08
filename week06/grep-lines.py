#!/usr/bin/env python3

import sys

pattern = sys.argv[1]

a = []
L = len(pattern)

s = input()
while s != "end":
    i = 0
    while i < len(s):
        if s[i: i + L] == pattern:
            a.append(s)
            i += len(s)
        i += 1
    s = input()

i = 0
while i < len(a):
    print(a[i])
    i += 1
