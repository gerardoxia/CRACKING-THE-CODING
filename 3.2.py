#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Node:
    def __init__(self,data):
        self.data=data
        self.LLnext=None
        self.data2=None
        #self.LLnext2=None
    def appendLL(self,d):
        end=Node(d);
        while(self.LLnext!=None): self=self.LLnext
        self.LLnext=end

class Stack:
	def __init__(self,data):
		self.top = Node(data)
		self.top.data2=data
		#self.top.LLnext2=self.top
	def pop(self):
		if(self.top != None ):
			item = self.top.data
			self.top = self.top.LLnext
			return item
	def push(self,data):
		temp = Node(data)
		temp.data2 = self.top.data2
		if(data<self.top.data2):
			temp.data2=data
			#self.top.LLnext=temp
		temp.LLnext = self.top
		self.top = temp
	def min(self):
		return self.top.data2

a=Stack(10)
a.push(9)
a.push(8)
a.push(7)
print(a.min())
a.pop()
print(a.min())
a.push(0)
print(a.min())
a.push(2)
print(a.min())



 