#!/usr/bin/env python3

a = []
s = input()
while s != "end":
    a.append(int(s))
    s = input()

i = 0
while i < len(a):
    j = 0
    while j < len(a):
        if a[j] > a[i]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
        j += 1
    i += 1
i = 0
while i < len(a):
    print(a[i])
    i += 1
