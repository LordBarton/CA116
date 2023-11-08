#!/usr/bin/env python3

n = int(input())
i = 0
s = ""

while i < n:
    m = int(input())
    s += chr(m)
    i += 1
i = 0
while i < n:
    t = (ord(s[i]))
    print(t * "*")
    i += 1
