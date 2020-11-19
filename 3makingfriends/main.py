#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 13:02:54 2020

@author: barre
"""
#contents = open("/Users/barre/Desktop/EDAF05-labs-public-master/3makingfriends/data/sample/2.in").read()

from queue import PriorityQueue
import fileinput

#sätter parent till sig själv och size = 1
def do_set(node):
    parents[node] = node
    size[node] = 1
    

def kruskal(G):
    #skapar set av noder för varje nod som skickas in.
    nodes = G['nodes']
    [do_set(node) for node in nodes]
    T = []
    #lägger alla kanter i en priokö med vikt som prio
    B = PriorityQueue()
    [B.put((int(edge[2]),edge)) for edge in G['edges']]
    while not B.empty():
        edge = B.get()[1]
        n1 = edge[0]
        n2 = edge[1]
        #kollar så att de inte skapar en cykel, om de kommer till samma find så gör de det.
        if find(n1) != find(n2):
            union(n1,n2)
            T.append(edge)
    
    return T
        

def union(u,v):
    u = find(u)
    v = find(v)
    if size[u]<size[v]:
        parents[u] = v
        size[v] = size[u] + size[v]
    else:
        parents[v] = u
        size[u] = size[u] + size[v]
        


def find(v):
    p = v
    while parents[p] != p:
        p = parents[p]
    while parents[v] != p:
        w = parents[v] #varför behövs denna?
        parents[v] = p
        v= w #varför behövs denna?
    
    return p
    

def make_graph(lines):
    nodes = set()
    edges = []
    for line in lines:
        nodes.add(line[0])
        nodes.add(line[1])
        edges.append(line)
    
    return {'nodes':nodes,'edges':edges}




parents = dict()
size = dict()

input_array = []
for line in fileinput.input():
    input_array.append(line.split(' '))


first_row = [int(x) for x in input_array[0]]
nbr_persons = first_row[0]
nbr_edges = first_row[1]

lines = []
for line in input_array[1:nbr_edges+1]:
    line[2] = line[2].rstrip('\n')
    lines.append(line)

G = make_graph(lines)
T = kruskal(G)
n = 0
for x in T:
    n = n + int(x[2])

print(n)

    
