# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 11:08:39 2018

@author: lb13
"""


class Queue(object):
    """ Queue with given max size """ 
    def __init__(self, maxSize=10):
        """ takes maxSize whose  default value is 10 """
        self.L = [None]*maxSize
        self.size = 0
        self.maxSize = maxSize
        self.tail = 0
        self.head = 0
    def enqueue(self,value):
        """ adds value to queue, raises exception if full """ 
        assert not self.isFull(), "Queue Full"
        self.L[self.tail]=value
        if self.tail<self.maxSize-1:
            self.tail+=1
        else: 
            self.tail = 0
        self.size+=1
    def dequeue(self):
        """ removes and returns first value in, raises exception if empty"""
        assert not self.isEmpty(), "Queue Empty"         
        val = self.L[self.head]
        if self.head<self.maxSize-1:
            self.head+=1
        else: 
            self.head=0
        self.size-=1         
        return val 
    def peakHead(self):
        """ returns value at head, raises exception if empty"""
        assert not self.isEmpty(), "Queue Empty"   
        return self.L[self.head] 
    def isFull(self):
        """ returns True if full"""
        return self.size==self.maxSize 
    def isEmpty(self):
        """ returns True if empty"""        
        return self.size==0
    def __str__(self):
        s = "["
        index  = self.head 
        count = 0
        while count!=self.size: 
            s = s+ str(self.L[index])+","
            if index<self.maxSize-1:
                index+=1
            else: 
                index=0
            count+=1
        if self.size!=0: 
            s = s[:-1]
        return s+"]"
    def __len__(self):
        return self.size 
		
