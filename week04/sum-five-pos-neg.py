#!/usr/bin/env python3

i = 0
ps = 0
ng = 0

while i < 5:
    n = int(input())
    if n < 0:
        ng += n
    else:
        ps += n
    i += 1
print(ng, ps)
