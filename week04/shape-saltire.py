#!/usr/bin/env python3

n = int(input())
m = n // 2
i = 0

if n == 1:
    print("*")
else:
    while i < m:
        print(" " * i + "*" + " " * (n - 2 * (i + 1)) + "*")
        i += 1
    print(" " * m + "*")
    i = 0
    p = m
    while i < m:
        print(" " * (p - 1) + "*" + " " * (i * 2 + 1) + "*")
        p -= 1
        i += 1
