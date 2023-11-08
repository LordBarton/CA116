#!/usr/bin/env python3

import sys
n = int(sys.argv[1])

s = "LatD,LatM,LatS,NS,LonD,LonM,LonS,EW,City,State"

j = 0
total = -1
while j < len(s) and total != n - 1:
    if s[j] == ",":
        total += 1
    j += 1
st = j
while j < len(s) and total != n:
    if j < len(s) and s[j] == ",":
        total += 1
    j += 1
if n == 0:
    print(s[:j - 1])
elif n == 9:
    print(s[st:j])
else:
    print(s[st:j - 1])
