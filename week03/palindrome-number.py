#!/usr/bin/env python3

n = int(input())
L = len(str(n))
i = 0
total = 0

while i < L:
    r = L - i - 1
    p = n // 10 ** i % 10
    q = n // 10 ** r % 10
    if p == q:
        total += 1
    i += 1

if total == L:
    print("yes")
else:
    print("no")
