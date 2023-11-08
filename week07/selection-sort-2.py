#!/usr/bin/env python3

s = input()
a = []

while s != "end":
    a.append(int(s))
    s = input()
t = int(input())

i = t
temp = a[t]
total = t
while i < len(a):
    if a[i] < temp:
        temp = a[i]
        total = i
    i += 1
print(total)
