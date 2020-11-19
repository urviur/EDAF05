#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 12:09:34 2020

@author: barre
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 10:19:00 2020

@author: barre
"""
import fileinput

#================ METODER ======================

def find_min_edges(E, C, s, t, cap, remove_list):
    #hur många kanter vi lagt till
    counter = 0
    n = len(C)
    flow = 0
    #res graf, alla kapaciteter är 0 från början. 
    F = [[0 for y in range(n)] for x in range(n)]
    #lägger till kanter så länge flödet är mindre än kapaciteten
    while flow<cap:
        while True:
            #parent
            path = [-1 for x in range(n)]
            path[s] = -2
            #möjlig capacitet för noden den ska till/motsvarande path
            cap_list = []
            cap_list = [0 for x in range(n)]
            cap_list[s] = 9999999
            BFSq = []
            BFSq.append(s)
            pathFlow, P = BFSEK(E, C, s, t, F, path, cap_list, BFSq)
            if pathFlow == 0:
                edge = index_edges[int(remove_list.pop()[0])]
                E[edge[0]].append(edge[1])
                E[edge[1]].append(edge[0])
                counter +=1
                break
            flow = flow + pathFlow
            v = t
            #ändrar kapaciteterna efter hur flödet ser ut.
            while v != s:
                u = P[v]
                F[u][v] = F[u][v] + pathFlow
                F[v][u] = F[v][u] - pathFlow
                v = u
            
    nbr_removed = M-counter+1
    return flow, nbr_removed

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
lines = []
for line in fileinput.input():
    line = line.replace('\n', '')
    lines.append(line.split(' '))



#===============================================

#======= MANUELL INLÄSNING AV DATA =============
#contents = open("/Users/barre/Desktop/EDAF05-labs-public-master/6railwayplanning/data/secret/1small.in").read()
#lines = [x.split(' ')for x in contents.split('\n')]

first_row  = lines[0];
N = int(first_row[0]) #nodes
M = int(first_row[1]) #edges
Cap = int(first_row[2]) #studentes/capacity
P = int(first_row[3]) #routes



#create c, e
E = [[] for x in range(N)] # grannar, inga från början
C = [[0 for y in range(N)] for x in range(N)] # kapacitetsmatris


s = 0 #start index 
t= N-1 #end index

edges_input = lines[1:M+1]
remove_list = lines[M+1:]
index_edges = []
#lägger in vikter
for e in edges_input:
    C[int(e[0])][int(e[1])] = int(e[2])
    C[int(e[1])][int(e[0])] = int(e[2])
    index_edges.append([int(e[0]),int(e[1])])

res = find_min_edges(E, C, s, t, Cap, remove_list)

print(str(res[1])+ ' ' + str(res[0]))
