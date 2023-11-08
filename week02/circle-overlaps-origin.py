#!/usr/bin/env python3

x = int(input())
y = int(input())
r = int(input())

dx = 0 - x
dy = 0 - y

print((dx * dx + dy * dy) < r * r)
