#!/usr/bin/env python3

s = input()
i = 0

while i < len(s) and (s[i] < "1" or s[i] > "9"):
    i += 1
j = i + 1
#print(i)
while j < len(s) and (s[j] >= "0" and s[j] <= "9"):
    j += 1
#print(j)
if i < len(s):
    print(s[i:j], i)
