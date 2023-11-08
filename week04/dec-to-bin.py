#!/usr/bin/env python3

n = int(input())
bin = ""

while n != 0:
    bin += str(n % 2)
    n = n // 2
i = len(bin)
bin2 = ""
while i > 0:
    bin2 += bin[i - 1]
    i -= 1
print(bin2)
