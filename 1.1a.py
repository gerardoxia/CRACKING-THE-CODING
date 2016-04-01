#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def unique(str):#最蠢，其实可以直接比较出现是否
    list1=list(str)
    flag=True
    for a in range(0,len(list1)-2):#双循环，从0到-2
        for b in range(a+1,len(list1)-1):#从上一层到-1,这里有问题-1和-2没有比较
            if list1[a]==list1[b]:
                flag=False
    if list1[-2]==list1[-1]:#不是很会用range，就把最后-1和-2的比较单独写
        flag=False
    return(print(flag))
unique(input())

