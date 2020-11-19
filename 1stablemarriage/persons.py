#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 09:09:52 2020

@author: barre
"""
import queue
 
class Man:
    
    
    #creates person
    def __init__ (self ,index, prefernceString):
        self.index = index
        #makes a preferncelist from a string.
        
        pl = prefernceString.split(' ')
       
        prioQueue = queue.SimpleQueue()
    
        #prioqueue
        for i in range(0,len(pl)):
            prioQueue.put(int(pl[i]))
            
        self.queue = prioQueue
        
        
        
        
class Woman:
    
    
    #creates person
    def __init__ (self ,index, prefernceString):
        self.index = index
        #makes a preferncelist from a string.
        
        ps = prefernceString.split(' ')
         
        pList = [''] * len(ps)
        
        
        #creates a inverted list
        for i in range(0,len(ps)):
            pList[int(ps[i])-1] = i + 1
            
        
        #the inverted list
        self.list = pList
        
        
        
        
        
        
    