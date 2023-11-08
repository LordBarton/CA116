#!/usr/bin/env python3

m = int(input())

print("first: " + str(m >= 70))
print("second: " + str(m >= 50 and m <= 69))
print("third: " + str(m >= 40 and m <= 49))
print("fail: " + str(m < 40))
