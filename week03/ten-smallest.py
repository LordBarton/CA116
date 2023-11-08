#!/usr/bin/env python3

i = 0
n = int(input())
ns = n
while i < 9:
    n = int(input())
    if ns > n:
        ns = n
        i += 1
    else:
        i += 1
print(ns)
