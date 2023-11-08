#!/usr/bin/env python3

n = input()
while n != "end":
    n1 = ""
    n2 = ""
    i = 0
    while n[i] != " ":
        n1 += n[i]
        i += 1
    i += 1
    while i < len(n):
        n2 += n[i]
        i += 1
    n1 = int(n1)
    n2 = int(n2)
    n3 = n1 + n2
    s = str(n1) + " + " + str(n2) + " = " + str(n3)
    n3s = str(n1) + " + " + str(n2) + "   "
    L = len(n3s)
    if L > 21:
        print(s)
    else:
        print(" " * (21 - L), s)
    n = input()
