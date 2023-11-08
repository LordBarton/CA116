#!/usr/bin/env python3

old = int(input())
new = int(input())

while new != 0:
    temp = old
    old = new
    new = temp % new
print(old)
