#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def partition(L,left,right):
    i=left
    for a in range(left,right):#只遍历到-2
        if L[a]<=L[right]:#用-1做标准
            L[a],L[i]=L[i],L[a]
            i=i+1
    L[i],L[right]=L[right],L[i]
    return i

def qs(L,left,right):
    if left>right:
        return
    index=partition(L,left,right)
    qs(L,left,index-1)
    qs(L,index+1,right)

a=[1,2,233243,1,0,5,2,35,12,8,12]
qs( a,0,len(a)-1 )
print( a ) 







