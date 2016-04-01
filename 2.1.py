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

def ifDupe(head):
    check1=head
    while(check1!=None):
        check2=check1
        while(check2.LLnext!=None):
            if(check1.data==check2.LLnext.data):
                check2.LLnext=check2.LLnext.LLnext
            else:check2=check2.LLnext
        check1=check1.LLnext

a=Node(5)
a.appendLL(1)
a.appendLL(5)
a.appendLL(5)
a.appendLL(5)
a.appendLL(5)
a.appendLL(1)


ifDupe(a)
print(a.LLnext.data)


