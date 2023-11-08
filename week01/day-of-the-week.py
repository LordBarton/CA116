#!/usr/bin/env python3

month = int(input())
day = int(input())
number = ((month - 1) * 30 + day)

print(number - 7 * ((number - 1) // 7))
