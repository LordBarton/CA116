#!/usr/bin/env python3

i = 0
s = ""

while i < 10:
    n = int(input())
    s += chr(n)
    i += 1
i = 0
while i < 10:
    print(ord(s[i]) * "*")
    i += 1
