#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 12:08:52 2020

@author: barre
"""

import queue



# Gale-Shapley algoritm is implemented
def GS(W,M):
    
    p = list(M)
    #woman is key, man is value
    pairs = {}
    while(len(p) != 0):
        #first man in the list is taken out of the list.
        m = p.pop(0)
        
        #the woman that is first in his queue is taken out from his queue.
        w = M[m].get()
        
        #if w has no partner
        if not (w in pairs):
            pairs[w] = m
        
        #w prefers m over her current partner
        elif(W[w][m-1]<W[w][pairs[w]-1]):
            #add her partner to the list
            p.append(pairs[w])
            #add her new partner
            pairs[w] = m
            
            
        #add m to p agian if if he dident get a partner
        else:
            p.append(m)
    
    return pairs
    
    
def MakeInvertedListWoman(rowList):
    
         
    pList = [''] * len(rowList)
    
    
    #creates a inverted list
    for i in range(0,len(rowList)):
        pList[rowList[i]-1] = i + 1
        
    
    #the inverted list
    return pList

def MakeFifoQueueMan(rowList):
       
    fifoQueue = queue.SimpleQueue()

    #fifoqueue
    for i in range(0,len(rowList)):
        fifoQueue.put(rowList[i])
        
    return fifoQueue


