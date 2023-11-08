#!/usr/bin/env python3

s = input()
i = 0
t = ""
count = 0

while i < len(s):
    c = ord(s[i])
    if ((c >= 97) and (c <= 122)) or ((c >= 65) and (c <= 90)):
        count += 1
        if (count % 2 == 0 and (c >= 97 and c <= 122)):
            ts = c - 32
            t += chr(ts)
        elif (count % 2 != 0 and (c >= 65 and c <= 90)):
            ts = c + 32
            t += chr(ts)
        else:
            t += s[i]
    else:
        t += s[i]
    i += 1
print(t)
