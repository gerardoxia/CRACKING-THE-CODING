#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def uniqueBit(str):
    i=0
    L=list(str)
    LL=len(L)
    count=0#重复的次数
    a=0#下标

    while a<LL-count:#因为删一个元素数组就短了 不设置就会越界
        j=ord(L[a])-ord('a')
        if(i&(1<<j)):
            del L[a]
            count=count+1#重复一次，并且下标不增加
            i=i|(1<<j)
        else:
            i=i|(1<<j)
            a=a+1#不重复，下标加1

    str=''.join(L)
    return str
print(uniqueBit(input()))


