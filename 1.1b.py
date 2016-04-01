#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

def qs(L):
    left=[]
    right=[]
    middle=[]
    if len(L)<2:
        return L
    else:
        pivot= random.choice(L)
        for a in L:
            if a<pivot:
                left.append(a)
            elif a>pivot:
                right.append(a)
            else:
                middle.append(a)
        return (qs(left)+middle+qs(right))

def unique(str):
    L=[]
    flag=True
    for a in range(0,len(str)):
        L.append(ord(str[a]))
    L=qs(L)

    b=0#
    for a in L[:-1]: #切片遍历 从0到-2
        if a==L[b+1]: #如果a和下一个元素相等
            flag=False
            return(print(L,flag))#
        b=b+1 
    return(print(L,flag))

unique(input())
