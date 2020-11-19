#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 19:49:14 2020

@author: barre
"""
import time
import fileinput

import queue

#nodklass
class Node:
    def __init__(self,name):
        self.name = name
        self.bfs_index = 0
        self.neighbours = []
        self.visited = False
        self.prod = None
    
    

def bfs(G,str_s,str_t):
#lika så är sträckan 0
    if str_s == str_t:
        print(0)
        return
    
    #sätter all index till 0 och gör första elementet till s
    for node in G:
        node.visited = False
        node.bfs_index = 0
        if node.name == str_s:
            s = node
            
    s.visited = True
    
    q = queue.SimpleQueue()
    
    q.put(s)
    
    while not q.empty():
        v = q.get()
        
        
        for w in v.neighbours:
            
            if not w.visited:
                w.prod = v
                w.bfs_index = v.bfs_index +1 
                w.visited = True
                q.put(w)
                
                if w.name == str_t:
                     #antalet kanter från s till t är index i nod
                    print(w.bfs_index)
                    print(w.name)
                    route(w)
                    return
                
    
    #    
    print('Impossible')
    

    
def route(node):
    
    if(node.prod == None):
        return
    else:
        print(node.prod.name)
        route(node.prod)
        return
        

# gör graf 
def make_graph(word_list):
    
    
    G = []
    # skapar G med noder av index och namn
    [G.append(Node(word_list[i])) for i in range(0,len(word_list))]
    
    for i in range(0,len(G)):
        node_1 = G[i]
        for j in range(0,i):
            node_2 = G[j]
            #kollar vilka som stämmer
            
            [arc12,arc21] = check_neighbour(node_1.name,node_2.name)
            
            #om arc12 är sann så lägger vi till neighbour
            if arc12:
                node_1.neighbours.append(node_2)
            
            if arc21:
                node_2.neighbours.append(node_1)
            
    return G
#            

#kollar neighbour
def check_neighbour(name_1,name_2):
    temp_1 = name_1
    temp_2 = name_2
    arc12 = True
    arc21 = True
    
    #om de fyra sista är i 
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



input_array = []
start_time = time.time()
#reads the input file into a list
for line in fileinput.input():
    input_array.append(line)


time_1 = time.time()


first_row = [int(x) for x in input_array[0].split(' ')]
N = first_row[0]
Q = first_row[1]

word_list = [x.rstrip('\n') for x in input_array[1:N+1]]
path_list = [x.rstrip('\n').split(' ') for x in input_array[N+1:N+Q+1]]

time_2 = time.time()

G = make_graph(word_list)

time_3 = time.time()

for path in path_list:
    bfs(G,path[0],path[1])

#print("--- %s inläsning ---" % (time_1 - start_time))
#
#print("--- %s wordlist osv ---" % (time_2 - time_1))
#
#print("--- %s göra graf ---" % (time_3 - time_2))
#
#print( "--- %s bfs ---" % (time.time() - time_3))
#n = 0
#for g in G:
#    n = n + len(g.neighbours)
#    
#print(n)