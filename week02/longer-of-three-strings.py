#!/usr/bin/env python3

a = input()
b = input()
c = input()

la = len(a)
lb = len(b)
lc = len(c)

if(la > lb and la > lc):
    print(a)
elif(lb > la and lb > lc):
    print(b)
else:
    print(c)
