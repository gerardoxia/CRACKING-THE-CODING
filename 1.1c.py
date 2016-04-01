#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def uniqueBit(str):
    i=0
    for a in str:
        j=ord(a)-ord('a')
        if(i&(1<<j)):
            print(i,j,i&(1<<j))
            return False
        print("@@@",i,j,i&(1<<j))
        i=i|(1<<j)
    return True
print(uniqueBit(input()))

