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

class Queue:
	def __init__(self,data):
		self.first = Node(data)
		self.last = self.first
	def dequeue(self):
		if(self.first != None ):
			item = self.first.data
			self.first = self.first.LLnext
			return item
	def enqueue(self,data):
		temp = Node(data)
		self.last.LLnext = temp
		self.last = temp


class MyQueue:
	def __init__(self,data):
		self.stack1 = Stack(data)
		self.stack2 = Stack(0)
		self.stack2.pop()
	def dequeue(self):
		if(self.stack1.top != None ):
			while(self.stack1.top != None):		
				temp = self.stack1.pop()
				self.stack2.push(temp)
			item = self.stack2.pop()
			while(self.stack2.top != None):		
				temp = self.stack2.pop()
				self.stack1.push(temp)
			return item
	def enqueue(self,data):
		self.stack1.push(data)

a=Queue(1)
a.enqueue(2)
a.enqueue(3)
a.enqueue(4)
print(a.dequeue())
print(a.dequeue())
print(a.dequeue())
print(a.dequeue())




