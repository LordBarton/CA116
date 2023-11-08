#!/usr/bin/env python3

a = []
s = input()
while s != "end":
    i = 0
    while i < len(a) and s != a[i]:
        i += 1
    if i == len(a):
        print(s)
    a.append(s)
    s = input()
