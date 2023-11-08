#!/usr/bin/env python3

s = input()
i = 0
j = 0

while i < len(s) // 2:
    if s[i] == s[len(s) - i - 1]:
        j += 1
    i += 1

if j == len(s) // 2:
    print("palindrome")
