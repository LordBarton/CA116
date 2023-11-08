#!/usr/bin/env python3

n = int(input())

n0 = 0
n1 = 1
n2 = 1
print(0)
while n1 < n:
    n2 = n0 + n1
    print(n1)
    n0 = n1
    n1 = n2
