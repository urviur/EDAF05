#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 10:19:00 2020

@author: barre
"""
import fileinput
import decimal

#================ METODER ======================

def EdmondsKarp(E, C, s, t):
    n = len(C)
    flow = 0
    F = [[0 for y in range(n)] for x in range(n)]
    while True:
        P = [-1 for x in range(n)]
        P[s] = -2
        M = [0 for x in range(n)]
        M[s] = decimal.Decimal('Infinity')
        BFSq = []
        BFSq.append(s)
        pathFlow, P = BFSEK(E, C, s, t, F, P, M, BFSq)
        if pathFlow == 0:
            break
        flow = flow + pathFlow
        v = t
        while v != s:
            u = P[v]
            F[u][v] = F[u][v] + pathFlow
            F[v][u] = F[v][u] - pathFlow
            v = u
    return flow

def BFSEK(E, C, s, t, F, P, M, BFSq):
    while (len(BFSq) > 0):
        u = BFSq.pop(0)
        for v in E[u]:
            if C[u][v] - F[u][v] > 0 and P[v] == -1:
                P[v] = u
                M[v] = min(M[u], C[u][v] - F[u][v])
                if v != t:
                    BFSq.append(v)
                else:
                    return M[t], P
    return 0, P


#===============================================


#================ LÄS IN DATA ==================
#lines = []
#for line in fileinput.input():
#    line = line.replace('\n', '')
#    lines.append(line.split(' '))
#
#first_row = lines[0]

#===============================================

#======= MANUELL INLÄSNING AV DATA =============
contents = open("/Users/barre/Desktop/EDAF05-labs-public-master/6railwayplanning/data/secret/1small.in").read()
lines = [x.split(' ')for x in contents.split('\n')]

first_row  = lines[0];
N = int(first_row[0]) #nodes
M = int(first_row[1]) #edges
Cap = int(first_row[2]) #studentes/capacity
P = int(first_row[3]) #routes



#create c, e
E = C = [[] for x in range(N)]
C = [[0 for y in range(N)] for x in range(N)]


s = 0 #start index 
t= N-1 #end index

edges_input = lines[1:M+1]
remove_list = lines[M+1:]
index_edges = []
#lägger in vikter och vägar
for e in edges_input:
    C[int(e[0])][int(e[1])] = int(e[2])
    C[int(e[1])][int(e[0])] = int(e[2])
    E[int(e[0])].append(int(e[1]))
    E[int(e[1])].append(int(e[0]))
    index_edges.append([int(e[0]),int(e[1])])



nbr_removed = 0
max_flow = EdmondsKarp(E,C,s,t)


for i in remove_list[:-1]:
    r = index_edges[int(i[0])]
    #ta bort noder i båda lisor

    temp_cap_a = C[int(r[0])][int(r[1])] 
    temp_cap_b = C[int(r[1])][int(r[0])]
    
    C[int(r[0])][int(r[1])] = 0
    C[int(r[1])][int(r[0])] = 0
    
    E[int(r[0])].remove(int(r[1]))
    E[int(r[1])].remove(int(r[0]))
    
#        
    #ny graf nu skapad.
    
    
    new_flow = EdmondsKarp(E,C,s,t)
    if new_flow >= Cap:
        max_flow = new_flow
        nbr_removed += 1
       
        
    else:
        #lägg tillbaka noderna
        C[int(r[0])][int(r[1])] = temp_cap_a
        C[int(r[1])][int(r[0])] = temp_cap_b
        E[int(r[0])].append(int(r[1]))
        E[int(r[1])].append(int(r[0]))
        

print(str(nbr_removed) + ' ' + str(max_flow))



