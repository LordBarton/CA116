#!/usr/bin/env python3


import sys
n = str(sys.argv[1])

s = "LatD,LatM,LatS,NS,LonD,LonM,LonS,EW,City,State"

i = 0
total = 0
while i < len(n):
    j = 0
    while j < len(s) and s[j:j + len(n)] != n:
        if s[j] == ",":
            total += 1
        j += 1
    i += 1
print(total // len(n))
