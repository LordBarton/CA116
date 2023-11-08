#!/usr/bin/env python3

s = input()
a = []

while s != "end":
    a.append(s)
    s = input()

i = 0
while i < len(a):
    j = 0
    while j < len(a):
        h = 0
        while h < len(a[i]) - 1 and a[i][h] == a[j][h]:
            h += 1

        if a[i][h:] < a[j][h:]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
        j += 1
    i += 1
i = 0
while i < len(a):
    print(a[i])
    i += 1
