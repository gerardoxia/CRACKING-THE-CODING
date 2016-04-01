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
        return qs(left)+middle+qs(right)
print(qs([101, 101, 118, 118, 119, 101, 118, 119, 101, 102, 119, 101, 102, 119, 101, 102]))
