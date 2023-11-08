#!/usr/bin/env python3

n = int(input())

if((n % 10 ** 2) != 11 and (n == 1 or n % 10 == 1)):
    print("st")
elif((n % 10 ** 2) != 12 and (n == 2 or n % 10 == 2)):
    print("nd")
elif((n % 10 ** 2) != 13 and (n == 3 or n % 10 == 3)):
    print("rd")
else:
    print("th")
