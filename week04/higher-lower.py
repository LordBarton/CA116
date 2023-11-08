#!/usr/bin/env python3

old = 0
new = 0
i = 0

old = int(input())
while i < 5:
    new = int(input())
    if new > old:
        print("higher")
    elif new < old:
        print("lower")
    else:
        print("equal")
    old = new
    i += 1
