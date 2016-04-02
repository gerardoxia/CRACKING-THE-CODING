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


def hanoi(n,src,bri,dst):
	if(n==1):
		dst.push(src.pop())
	else:
		hanoi(n-1, src, dst, bri);
		dst.push(src.pop())
		hanoi(n-1, bri, src, dst);

n = 6;

A=Stack(6)
A.push(5)
A.push(4)
A.push(3)
A.push(2)
A.push(1)

B=Stack(1)
B.pop()
C=Stack(1)
C.pop()
hanoi(n, A, B, C);

print(C.pop())
print(C.pop())
print(C.pop())
print(C.pop())
print(C.pop())
print(C.pop())