#!/usr/bin/env python3

a = int(input())
b = int(input())

if a % 2 == 0 and (b == a // 2):
    print("yes")
elif a % 2 != 0 and (b == 3 * a + 1):
    print("yes")
else:
    print("no")
