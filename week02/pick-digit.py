#!/usr/bin/env python3

n = int(input())
p = int(input())
position = (n % 10 ** (p + 1))

print(position // 10 ** p)
