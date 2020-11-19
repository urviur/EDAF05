#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 23:02:30 2020

@author: barre
"""

import queue

class Node:
    def __init__(self,name, index):
        self.name = name
        self.index = index
        self.neighbours = []
        self.visited = False
    
    

def bfs(G,s,t):
    for node in G:
        if node.name == s:
            node.visited = True
            first_node = node
        
        else:
            node.visited = False
    
    q = queue.SimpleQueue()
    q.put(first_node)
    counter = 1
    while not q.empty():
        v = q.get()
        for w in v.neighbours:
            w.visited = True
            q.put(w)
            if w.name == t:
                return counter
            
        counter +=1
        
    return "Impossible"
            
    
    

##    
def make_graph(word_list):
    
    
    G = []
    # skapar G med noder av index och namn
    [G.append(Node(word_list[i],i)) for i in range(0,len(word_list))]
    
    for node_1 in G:
        for node_2 in G:
            #om de är samma, break forloopen
            if node_1.index == node_2.index:
                break
            
            #kollar vilka som stämmer
            
            [arc12,arc21] = check_neighbour(node_1.name,node_2.name)
            
            #om arc12 är sann så lägger vi till neigbour
            if arc12:
                node_1.neighbours.append(node_2)
            
            if arc21:
                node_2.neighbours.append(node_1)
            
    return G
#            


def check_neighbour(name_1,name_2):
    temp_1 = name_1
    temp_2 = name_2
    arc12 = True
    arc21 = True
    
    
    for l in name_1[1:]:
        if l in temp_2:
            temp_2 = temp_2[:temp_2.find(l)] + temp_2[temp_2.find(l)+1:]
        else:
            arc12 = False
            break
    
    
    for l in name_2[1:]:
        if l in temp_1:
            temp_1 = temp_1[:temp_1.find(l)] + temp_1[temp_1.find(l)+1:]
        else:
            arc21 = False
            break
    
    return [arc12,arc21]




