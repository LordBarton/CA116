#!/usr/bin/env python3

n = int(input())

print(n % 400 == 0 or (n % 4 == 0 and n % 100 != 0))
