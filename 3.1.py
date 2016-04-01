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



a=Stack("aaa")
print(a.top.data)
a.push("qqq")
print(a.top.data)
print(a.pop())
print(a.top.data)
