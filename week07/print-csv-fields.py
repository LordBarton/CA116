#!/usr/bin/env python3

a = []
s = input()

while s != "end":
    a.append(s)
    s = input()

n = int(input())

i = 0
while i < len(a):
    j = 0
    while j < len(a[i]) and a[i][j] != ",":
        j += 1
    st = j
    j += 1
    while j < len(a[i]) and a[i][j] != ",":
        j += 1
    nd = j
    j += 1
    while j < len(a[i]) and a[i][j] != ",":
        j += 1
    rd = j

    if n == 0:
        print(a[i][:st])
    elif n == 1:
        print(a[i][st + 1:nd])
    elif n == 2:
        print(a[i][nd + 1:rd])
    i += 1
