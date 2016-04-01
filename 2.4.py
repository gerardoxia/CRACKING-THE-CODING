#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Node:
    def __init__(self,data):
        self.data=data
        self.LLnext=None
    def appendLL(self,d):
        end=Node(d);
        while(self.LLnext!=None): self=self.LLnext
        self.LLnext=end

def addLL(a,b):
    carry=0
    c=Node(0)
    while(a!=None or b!=None):
        temp=0
        if(a!=None): 
            temp=temp+a.data
            a=a.LLnext
        if(b!=None): 
            temp=temp+b.data
            b=b.LLnext
        temp=temp+carry
        carry=temp//10
        temp=temp%10
        c.appendLL(temp)
    return(c.LLnext)

a=Node(7)
a.appendLL(6)
a.appendLL(5)
b=Node(4)
b.appendLL(3)
b.appendLL(2)
b.appendLL(1)
c=addLL(a,b)
print(c.data)
print(c.LLnext.data)
print(c.LLnext.LLnext.data)
print(c.LLnext.LLnext.LLnext.data)
