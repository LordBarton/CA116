#!/usr/bin/env python3

s = input()
i = 0
while i < len(s) and s[i] != ".":
    i += 1
if i == len(s):
    print(s + "." + "0")
elif i == 0:
    print("0" + s)
elif s[len(s) - 1] == ".":
    print(s + "0")
elif s[0] == "-" and s[1] == ".":
    print("-" + "0" + s[1:])
else:
    print(s)
