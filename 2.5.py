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

def findbegin(a):
    if(a==None):return(print("empty link"))
    check=a
    checkD={}
    while(check!=None):
        if(check in checkD):
            print(check.data)
            return check
        checkD[check]=True
        check=check.LLnext

a=Node(1)
a.appendLL(2)
a.appendLL(3)
a.appendLL(4)
a.appendLL(5)
a.appendLL(6)
a.appendLL(7)
a.appendLL(8)

b=a.LLnext.LLnext.LLnext
c=a.LLnext.LLnext.LLnext.LLnext.LLnext.LLnext
c.LLnext=b
findbegin(a)
