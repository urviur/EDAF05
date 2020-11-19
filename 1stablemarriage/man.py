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
        #puts preferenslist 
        numberOfPersons = len(pl)
        prioQueue = queue.SimpleQueue()
    
        
        for i in range(0,numberOfPersons):
            prioQueue.put(int(pl[i]))
            
        self.prioQueue = prioQueue
        
        
        
        
class Woman:
    
    
    #creates person
    def __init__ (self ,index, prefernceString):
        self.index = index
        #makes a preferncelist from a string.
        
        pl = prefernceString.split(' ')
        #puts preferenslist 
        numberOfPersons = len(pl)
        
        
        
        
        
        
        
    