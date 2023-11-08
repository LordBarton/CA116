#!/usr/bin/env python3

n = int(input()) - 1
m = int(input())
i = 0
print(m)
while i < n:
    if m % 2 == 0:
        m //= 2
        print(m)
    else:
        m = m * 3 + 1
        print(m)
    i += 1
