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

def findLL(head,n):
    check1=head
    check2=head
    index=1
    while(check1.LLnext!=None):
        check1=check1.LLnext
        if(index>=n):
            check2=check2.LLnext
        index=index+1
    print(check2.data)

'''def findLL(head,n):
    check1=head
    check2=head
    index1=0
    index2=1
    while(check1!=None):
        check1=check1.LLnext
        index1=index1+1
    while(check2!=None):
        if(index2==index1+1-n):
            print(check2.data)
        check2=check2.LLnext
        index2=index2+1'''



a=Node(7)
a.appendLL(6)
a.appendLL(5)
a.appendLL(4)
a.appendLL(3)
a.appendLL(2)
a.appendLL(1)
findLL(a,7)



