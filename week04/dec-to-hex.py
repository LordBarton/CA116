#!/usr/bin/env python3

n = int(input())
t = ""
t1 = ""
s = "abcdef"
while n != 0:
    m = n % 16
    if m > 9:
        t += s[m - 10]
    else:
        t += str(m)
    n = n // 16
i = len(str(t))
while i > 0:
    t1 += t[i - 1]
    i -= 1
print(t1)
