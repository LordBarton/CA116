#!/usr/bin/env python3

a = []
s = input()
while s != "end":
    a.append(int(s))
    s = input()

b = []
s = input()
while s != "end":
    a.append(int(s))
    s = input()

i = 0
while i < len(a):
    j = 0
    while j < len(a):
        if a[i] < a[j]:
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp
        j += 1
    i += 1

i = 0
while i < len(a):
    print(a[i])
    i += 1
