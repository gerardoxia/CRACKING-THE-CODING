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

class SetOfStacks:
	def __init__(self,data):
		self = Stack(data)
		self.count = 1
		self.index = 1
	def pop(self):
		if(self.top != None):
			item = self.top.data
			self.top = self.top.LLnext
		return item
	def push(self,data):
		if(self.count < 2):
			temp = Node(data)
			temp.LLnext = self.top
			self.top = temp
			self.count=self.count+1
		else:
			temp=Stack(data)
			self.index=self.index+1
			temp.top.LLnext=self.top
			self.top=temp.top
			self.count=1

a=SetOfStacks(1)
print(repr(a.top.data),"  count:  "+repr(a.count)+"  index: "+repr(a.index))
a.push(2)
print(repr(a.top.data),"  count:  "+repr(a.count)+"  index: "+repr(a.index))
a.push(3)
print(repr(a.top.data),"  count:  "+repr(a.count)+"  index: "+repr(a.index))
