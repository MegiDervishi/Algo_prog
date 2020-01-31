from collections import defaultdict
import math

def get_neighbours(madj,v):
    n = set()
    for i in range(len(madj)):
        if madj[v][i] != 0: 
            n.add(i)
    return n

def extractmins(Q,dist):
    lu = []
    mincost = math.inf
    for i in Q:
        if dist[i] < mincost and dist[i] != math.inf:
            lu = [i]
            mincost = dist[i]
        elif dist[i] == mincost and dist[i] != math.inf:
            lu.append(i)
            
    return lu

def dijkstra(madj,s,t,u1,v1):
    dist = { i: math.inf for i in range(len(madj))}
    prev = defaultdict(list)
    Q = set(i for i in range(len(madj))) #not visited set of vertices
    dist[s] = 0
    while len(Q) > 0:
        lu = extractmins(Q,dist)
        for u in lu:
            Q.remove(u)
            if dist[u] == math.inf: break
            for v in get_neighbours(madj,u):
                alt = dist[u] + madj[u][v]
                if alt <= dist[v]:
                    dist[v] = alt
                    prev[v].append(u)
    return prev

def pathfinder(madj,s,u,v,curr, prev):
    if curr == s: return False
    elif curr == v and (u in prev[curr]): return True
    elif curr == v and (u not in prev[curr]): return False
    l = []
    for i in prev[curr]: 
        l.append(pathfinder(madj,s,u,v, i, prev))
    if True in l: return True
    else: return False
    
def short_edge(madj,s,t,u,v):
    prev = dijkstra(madj,s,t,u,v)
    return pathfinder(madj,s,u,v,t, prev)

def period(T):
    return T in (T+T)[1:-1]

madj = [[0,1,2,2,0],[0,0,2,0,0],[0,0,0,0,2],[0,0,0,0,2],[0,0,0,0,0]]
s = 0
t = 4
u = 0
v = 2
print(short_edge(madj, s, t, u, v))
