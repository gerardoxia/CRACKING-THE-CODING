#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''def reverse(str):
    for a in range(len(str)//2):
        temp=str[a]
        print(temp)
        str=str[:a+1]+str[len(str)-1-a]+str[a+2:]
        print(str[a])
        str=str[:len(str)-a]+temp+str[len(str)-a+1:]
    return
a=input()
reverse(a)
print(a)'''

str=''
str=str.join(['ab','b','c','d'])
print(str)

