#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 17:21:47 2020

@author: barre
"""
import queue
import fileinput

#================ Klasser ======================
class Node:
    def __init__(self,name):
        self.name = name
        self.neighbours = []
    

class Edge:
    def __init__(self, node_a,node_b, capacity):
        self.node_a = node_a
        self.node_b = node_b
        self.capacity = capacity
        self.flow = 0
        
    def get_potential_flow(self, node):
        #ut från denna
        if(node == self.node_a):
            return self.capacity - self.flow
        
        else:
            return -(self.capacity + self.flow)
        
    
    def change_flow(self,node,value):
        if(node == self.node_a):
            self.flow += value
        
        else:
            self.flow -= value
        
    
    
    
    
#==============================================

#================ METODER ======================



#
def bfs(s,t,G):
    
    path_list = dict()
    visited = []
    q = queue.SimpleQueue()
    q.put(s)
    while not q.empty():
        v = q.get()
        if(v == s):
            return 'path' #
        
        
#
#    



    

#==============================================

#================ LÄS IN DATA ==================
#lines = []
#for line in fileinput.input():
#    line = line.replace('\n', '')
#    lines.append(line.split(' '))
#
#first_row = lines[0]

#===============================================

#======= MANUELL INLÄSNING AV DATA =============
contents = open("/Users/barre/Desktop/EDAF05-labs-public-master/6railwayplanning/data/secret/0mini.in").read()
lines = [x.split(' ')for x in contents.split('\n')]

first_row  = lines[0];
N = int(first_row[0]) #nodes
M = int(first_row[1]) #edges
C = int(first_row[2]) #studentes/capacity
P = int(first_row[3]) #routes




s = 0 #start index 
t= N-1 #end index

edges = lines[1:M+1]
pref_list = lines[M+1:]

edges_list = []
nodes = dict()


#lista med edges, dict med noder som har sina grannar som value i form av lista (kanske bra med gueue sen?)
for e in edges:
    temp_edge = Edge(int(e[0]),int(e[1]),int(e[2]))
    edges_list.append(temp_edge)
    if int(e[0]) not in nodes:
        nodes[int(e[0])] = [temp_edge]
        
    elif int(e[0]) in nodes:
        nodes[int(e[0])].append(temp_edge)
       
    if int(e[1]) not in nodes:
        nodes[int(e[1])] = [temp_edge]
        
    elif int(e[1]) in nodes:
        nodes[int(e[1])].append(temp_edge)
    
    


path = bfs(nodes[0],nodes[N-1])






#===============================================

