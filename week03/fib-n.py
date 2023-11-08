#!/usr/bin/env python3

n = int(input())
i = 0
m1 = 0
m2 = 1
while i < n:
    print(m1)
    m3 = m2
    m2 += m1
    m1 = m3
    i += 1
