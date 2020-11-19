#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 20:53:03 2020

@author: barre
"""

import fileinput
import copy

def BFS(paths, cap, s, t, F, pot_flow):
    q = [s]
    #Parent håller koll på föregångare för en viss nod
    parent = [-1 for x in range(N)]
    parent[s] = -2
    #Loopa igenom så länge vi har noder
    while len(q) > 0:
        u = q.pop(0)
        for v in paths[u]:
            #Om det möjliga är större än noll och v har en parent (ej besökt).
            if cap[u][v] - F[u][v] > 0 and parent[v] == -1:
                parent[v] = u
                #Släpa med minsta capaciteten
                pot_flow[v] = min(pot_flow[u], cap[u][v] - F[u][v])
                if v != t:
                    q.append(v)
                else:
                    #Returnera potenitellt flöde + parentslista
                    return pot_flow[t], parent
    #Return noll i pot flow och parent
    return 0, parent

def find_min_edges(N, C, paths, cap, reEdge, edges):
    nbr_added = 0
    s = 0
    t = N - 1
    flow = 0
    #Graf för flöden, sätt till 0 först.
    F = [[0 for y in range(N)] for x in range(N)]
    #Lägg till kant bakifrån så länge flödet understiger nbr students.
    while flow < C:
        while True:
            #möjligt flöde
            pot_flow = [0 for x in range(N)]
            pot_flow[s] = 99999
            #Hitta en väg och returnera flöde samt lista med parents till varje nod
            pot_flow, parent = BFS(paths, cap, s, t, F, pot_flow)
            #Om potentiella flödet noll, lägg till en nod (nod som vi minst vill ta bort) och försök hitta väg igen.
            if pot_flow == 0:
                edge = edges[reEdge.pop()]
                paths[edge[0]].append(edge[1])
                paths[edge[1]].append(edge[0])
                nbr_added += 1
                break
            #Annars, öka flödet med detsamma
            flow = flow + pot_flow
            #Loopa genom vägen och ändra flödet
            v = t
            while v != s:
                u = parent[v]
                F[u][v] = F[u][v] + pot_flow
                F[v][u] = F[v][u] - pot_flow
                v = u
    return flow, nbr_added
    
#================ LÄS IN DATA ==================
lines = []
for line in fileinput.input():
    line = line.replace('\n', '')
    lines.append(line.split(' '))



#===============================================

#======= MANUELL INLÄSNING AV DATA =============
#contents = open("/Users/gustavbroman/Desktop/EDAF05-labs-public-master/6railwayplanning/data/secret/3large.in").read()
#lines = [x.split(' ')for x in contents.split('\n')]
#===============================================

#======== Main =================================

#tar emot inparameterar
firstLine = lines[0]
N = int(firstLine[0])
M = int(firstLine[1])
C = int(firstLine[2])
P = int(firstLine[3])

#sparar ner edges som startnod, slutnod, kapacitet med key index för kanten.
#paths: key med nodnummer å dess grannar
#caps: Kapaciteter för kanterna (matris)
edges = dict()
paths = dict()
cap = [[0 for y in range(N)] for x in range(N)]

# ---------- Hantering av indata -----------
for i in range(1,M+1):
    line = lines[i]
    edges[i-1] = [int(line[0]), int(line[1]), int(line[2])]
    
    if int(line[0]) not in paths:
        paths[int(line[0])] = [int(line[1])]
    else:
        paths[int(line[0])].append(int(line[1]))
    if int(line[1]) not in paths:
        paths[int(line[1])] = [int(line[0])]
    else: 
        paths[int(line[1])].append(int(line[0]))

    cap[int(line[0])][int(line[1])] = int(line[2])
    cap[int(line[1])][int(line[0])] = int(line[2])

reEdge = []
for i in range(P):
    line = lines[M+1+i]
    reEdge.append(int(line[0]))
    removeEdge = edges[int(line[0])]
    paths[removeEdge[0]].remove(removeEdge[1])
    paths[removeEdge[1]].remove(removeEdge[0])
    
# --------------------------------

flow, nbr_added = find_min_edges(N, C, paths, cap, reEdge, edges)

print(str(P-nbr_added+1) + " " + str(flow))