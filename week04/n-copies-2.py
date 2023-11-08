#!/usr/bin/env python3

s = input()
n = int(input())
i = 0
t = ""

t += (s + "-") * n

print(t[:len(t) - 1])
