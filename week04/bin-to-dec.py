#!/usr/bin/env python3

n = int(input())
i = 0
L = len(str(n))
total = 0

while i < L:
    total += n % 10 * (2 ** i)
    n = n // 10
    i += 1

print(total)
