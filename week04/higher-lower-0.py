#!/usr/bin/env python3

old = int(input())
while old != 0:
    new = int(input())
    if new == 0:
        old == 0
    elif new > old:
        print("higher")
    elif new < old:
        print("lower")
    else:
        print("equal")
    old = new
