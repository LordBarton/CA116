#!/usr/bin/env python3

x1 = int(input())
y1 = int(input())
r1 = int(input())

x2 = int(input())
y2 = int(input())
r2 = int(input())

dx = x1 - x2
dy = y1 - y2
rr = r1 + r2

if(dx * dx + dy * dy < rr * rr):
    print("yes")
else:
    print("no")
