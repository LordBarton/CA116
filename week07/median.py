#!/usr/bin/env python3

s = input()
a = []
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

m = len(a) // 2
if len(a) % 2 == 0 and a[m - 1] > a[m]:
    print(a[m - 1])
else:
    print(a[m])
