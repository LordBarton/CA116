#!/usr/bin/env python3

a = []
s = input()
while s != "end":
    a.append(s)
    s = input()

i = 0
while i < len(a):
    j = 0
    while j < len(a):
        if a[i][6:8] < a[j][6:8]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
        elif a[i][6:8] == a[j][6:8]:
            if a[i][3:5] < a[j][3:5]:
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
            elif a[i][3:5] == a[j][3:5]:
                if a[i][:2] < a[j][:2]:
                    temp = a[i]
                    a[i] = a[j]
                    a[j] = temp
        j += 1
    i += 1

i = 0
while i < len(a):
    print(a[i][9:])
    i += 1
