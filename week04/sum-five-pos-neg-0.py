#!/usr/bin/env python3

ps = 0
ng = 0

n = int(input())
while n != 0:
    if n < 0:
        ng += n
    else:
        ps += n
    n = int(input())
print(ng, ps)
