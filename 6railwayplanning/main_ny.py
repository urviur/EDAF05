import fileinput
import queue

#================ Klasser ======================
class Node:
    def __init__(self,name):
        self.name = name
        self.neighbours = []
    
class Edge:
    def __init__(self, node_a,node_b, capacity):
        self.node_a = node_a
        self.node_b = node_b
        self.initial_capacity = capacity
        
        self.flow_ab = 0
        
    # Returns the possible front flow and backflow
    def get_pot_flow(self):
        if self.flow_ab > 0:
            return [self.initial_capacity - self.flow_ab, self.initial_capacity + self.flow_ab]
        else:
            return [self.initial_capacity + self.flow_ab, self.initial_capacity - self.flow_ab]

    def change_flow(self, value):
        self.flow_ab = self.flow_ab + value

#==============================================

#================ METODER ======================

#def bfs(s,t):
#    
#    path_list = dict()
#    visited = []
#    q = queue.SimpleQueue()
#    q.put(s)
#    while not q.empty():
#        v = q.get()
#        if(v == s):
#            return 'path'
def bfs(s,t):
    q = queue.SimpleQueue()
    q.put(s)
    #not_visited = list(nodes)
    #not_visited.remove(s)
    visited = [s]
    pred = {}
    
    
    while not q.empty():
        n = q.get()
        if n == t:
            return get_path(s,t,pred)
        
        for w in nodes[n].neighbours:
            #Kolla kapaciteten
            e = edges[(min(n,w),max(n,w))]       
            #Kolla potentiella flödet från n till w
            if(w>n):
                pot_flow = e.get_pot_flow()[0]
            else:
                pot_flow = e.get_pot_flow()[1]
            
            if pot_flow != 0 and w not in visited:
                q.put(w)

                visited.append(w)

                pred[w] = n
    #Ingen väg!
    return None
                

def get_path(s,t,pred):
    min_delta = 99999
    path = [t]
    p = pred[t]
        
    c = edges[(p,t)].get_pot_flow()[0]
    min_delta = min(min_delta,c)
    
    while p != s:
        path.append(p)
        if pred[p] > p:
            #Frontflow
            c = edges[(p,pred[p])].get_pot_flow()[0]
            min_delta = min(min_delta,c)
        else:
            c = edges[(pred[p],p)].get_pot_flow()[1]
            min_delta = min(min_delta,c)
        if pred[p] == s:
            c = edges[(s,p)].get_pot_flow()[0]
            min_delta = min(min_delta,c)
        p = pred[p]
    path.append(s)
    path.reverse()
    return path, min_delta


def ford_fulkerson(s,t):
    path = bfs(s,t)
    flow = 0
    while path != None and path[1] >0:
        delta = path[1]
        for n in range(0,len(path[0])-1):
            if path[0][n] < path[0][n+1]:
                #Forwardflow
                e = edges[(path[0][n],path[0][n+1])]

                e.change_flow(delta)
                
            else:
                #Backflow
                e = edges[(path[0][n+1],path[0][n])]
                e.change_flow(-delta)
                
        flow += delta
        path = bfs(s,t)
        
    return flow
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
Cap = int(first_row[2]) #studentes/capacity
P = int(first_row[3]) #routes


s = 0 #start index 
t= N-1 #end index

edges_input = lines[1:M+1]
remove_list = lines[M+1:]


edges = dict()
nodes = dict()

nodeSeen = []

#lista med edges, dict med noder som har sina grannar som value i form av lista (kanske bra med gueue sen?)
for e in edges_input:
    a = min(int(e[0]),int(e[1]))
    b = max(int(e[0]),int(e[1]))
    w = int(e[2])
    
    new_edge = Edge(a,b,w)
    edges[(a,b)] = new_edge
    
    #Om ej tidigare setts
    if a not in nodeSeen:
        nodes[a] = Node(a)
        nodeSeen.append(a)
    if b not in nodeSeen:
        nodes[b] = Node(b)
        nodeSeen.append(b)
    
    nodes[a].neighbours.append(b)
    nodes[b].neighbours.append(a)


#print('In between goes flow')
#fl = ford_fulkerson(s,t)
#print(fl)
#print('----')
#
#temp_edge = edges.pop((3,4),None)
#nodes[3].neighbours.remove(4)
#nodes[4].neighbours.remove(3)
#
#print('Flow after removing 1,2')
#fw = ford_fulkerson(s,t)
#print(fw)
#print('----')
nbr_removed = 0
max_flow = ford_fulkerson(s,t)

#Save original graph
#latest_working_G = [edges, nodes]
index_edges = list(edges)

for e in remove_list[:-1]:
    e = int(e[0])
    n1 = index_edges[e][0]
    n2 = index_edges[e][1]
    
    for i in edges:
        edges[i].flow_ab = 0
    
    temp_edge = edges.pop((min(n1,n2),max(n1,n2)),None)
    nodes[n1].neighbours.remove(n2)
    nodes[n2].neighbours.remove(n1)

    new_flow = ford_fulkerson(s,t)
    
    #print(new_flow)
    #Remove edge from dictionary and as neighbours for node
    if new_flow >= Cap:
        max_flow = new_flow
        nbr_removed += 1
        print('delete ' + str(temp_edge.node_a) + ' to ' + str(temp_edge.node_b) + '. nbr_removed: ' + str(nbr_removed) + 'for flow =' + str(new_flow))
        
    else:
        #temp_edge.flow_ab = 0
        edges[(min(n1,n2),max(n1,n2))] = temp_edge
        nodes[n1].neighbours.append(n2)
        nodes[n2].neighbours.append(n1)
        print('Try to remove ' + str(temp_edge.node_a) + ' to ' + str(temp_edge.node_b) + ' not succ, nbr: ' + str(nbr_removed) + 'for flow =' + str(new_flow))

print(str(nbr_removed) + ' ' + str(max_flow))