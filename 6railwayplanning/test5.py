import fileinput
import copy

def BFS(paths, cap, s, t, F, parent, mF, bfs):
    while len(bfs) > 0:
        u = bfs.pop(0)
        for v in paths[u]:
            if cap[u][v] - F[u][v] > 0 and parent[v] == -1:
                parent[v] = u
                mF[v] = min(mF[u], cap[u][v] - F[u][v])
                if v != t:
                    bfs.append(v)
                else:
                    return mF[t], parent
    return 0, parent

def find_min_edges(N, C, paths, cap, reEdge, edges):
    i = 0
    s = 0
    t = N - 1
    flow = 0
    F = [[0 for y in range(N)] for x in range(N)]
    while flow < C:
        while True:
            parent = [-1 for x in range(N)]
            parent[s] = -2
            mF = [0 for x in range(N)]
            mF[s] = 99999
            bfs = []
            bfs.append(s)
            pathF, parent = BFS(paths, cap, s, t, F, parent, mF, bfs)
            if pathF == 0:
                edge = edges[reEdge.pop()]
                paths[edge[0]].append(edge[1])
                paths[edge[1]].append(edge[0])
                i += 1
                break
            flow = flow + pathF
            v = t
            while v != s:
                u = parent[v]
                F[u][v] = F[u][v] + pathF
                F[v][u] = F[v][u] - pathF
                v = u
    return flow, i
    
#================ LÄS IN DATA ==================
lines = []
#for line in fileinput.input():
#    line = line.replace('\n', '')
#    lines.append(line.split(' '))
#
#

#===============================================

#======= MANUELL INLÄSNING AV DATA =============
contents = open("/Users/barre/Desktop/EDAF05-labs-public-master/6railwayplanning/data/secret/3large.in").read()
lines = [x.split(' ')for x in contents.split('\n')]
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
#caps:
edges = dict()
paths = dict()
cap = [[0 for y in range(N)] for x in range(N)] # kapacitetsmatris

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

reEdge_temp = copy.deepcopy(reEdge)
for j in range(P):
    first = reEdge_temp.pop()
    removeEdge = edges[first]
    paths[removeEdge[0]].remove(removeEdge[1])
    paths[removeEdge[1]].remove(removeEdge[0])

flow, i = find_min_edges(N, C, paths, cap, reEdge, edges)

print(str(P-i+1) + " " + str(flow))