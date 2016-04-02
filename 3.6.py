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

class Stack:
	def __init__(self,data):
		self.top = Node(data)
	def pop(self):
		if(self.top != None ):
			item = self.top.data
			self.top = self.top.LLnext
			return item
	def push(self,data):
		temp = Node(data)
		temp.LLnext = self.top
		self.top = temp
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

def sortStack(stk):
	temp=[]
	while(stk.top!=None):
		temp.append(stk.pop())
	qs(temp,0,len(temp)-1 )
	for sel in temp:
		stk.push(sel)
	return(stk)

	


A=Stack(2)
A.push(34)
A.push(1)
A.push(13)
A.push(6)
A.push(3)
sortStack(A)
print(A.pop())
print(A.pop())
print(A.pop())
print(A.pop())
print(A.pop())
print(A.pop())

