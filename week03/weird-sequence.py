#!/usr/bin/env python3

n = int(input())
v = 0

i = 0
while i < n:
   print(v)
   v = -v + (v % 2 * 2 - 1)
   i = i + 1
