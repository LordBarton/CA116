#!/usr/bin/env python3

s = input()
a = []
while s != "end":
    a.append(int(s))
    s = input()

i = 0
temp = a[0]
while i < len(a):
    if a[i] < temp:
        temp = a[i]
    i += 1
print(temp)
