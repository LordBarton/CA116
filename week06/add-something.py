#!/usr/bin/env python3

a = []

s = input()
while s != "end":
    a.append(int(s))
    s = input()
i = 0
n = int(input())
while i < len(a):
    print(a[i] + n)
    i += 1
