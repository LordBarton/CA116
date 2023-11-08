#!/usr/bin/env python3

n = int(input())
v = n // 2
i = 0

if n == 1:
    print("*")
else:
    while i < v:
        print(" " * v + "*")
        i += 1
    i = 0
    print("*" * n)
    while i < v:
        print(" " * v + "*")
        i += 1
