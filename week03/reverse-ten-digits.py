#!/usr/bin/env python3

i = 0
m = 0
while i < 10:
    n = int(input())
    m = m + n * 10 ** (i + 1)
    i += 1
i = 0
while i < 10:
    print((m // 10 ** (10 - i)) % 10)
    i += 1
