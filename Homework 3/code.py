#exercise 1
def union_find(M):
    n = len(M)
    data = [i for i in range(n)]
    for i in range(n):
        for j in range(n):
            if find(data,i) != find(data,j):
                for k in range(n):
                    if data[k] == data[i]:
                        data[k] = data[j]


#Exercise 6

def h_index(A):
    n = len(A)
    if n==0: return 0
    #countsort
    cs = [0 for _ in range(n+1)]
    for c in A:
        cs[ min(n,c)] += 1
    h = 0
    for i in range(n,-1,-1):
        h += cs[i]
        if h >= i:
            return i
    return 0 #no index found
        
#Exercise 5
def friend_groups(M):
    #Union-Find
    n = len(M)
    count = n
    data = [i for i in range(n)]
    for i in range(n):
        r1 = find(data,i)
        for j in range(i+1,n):
            r2 = find(data,j)
            if r1 != r2 and M[i][j] == 1:
                count -= 1
                data[r2] = r1
    return data
    return count
    
def find(data,i):
    if i != data[i]:
        data[i] = find(data, data[i])
    return data[i]

"""M = [[1,1,0,0,0,0],
     [1,1,1,1,0,0],
     [0,1,1,0,0,0],
     [0,1,0,1,0,0],
     [0,0,0,0,1,1],
     [0,0,0,0,1,1]]"""


#Exercise 4
def course_schedule(n, prerequisites):
    #create graph
    graph = dict()
    for i in range(n): graph[i] = set() #no graph[0]=[4,4]
    for p in prerequisites:
        if p[0] in range(n) and p[1] in range(n):
            graph[p[0]].add(p[1])
        else:
            print("false"); return #n=2 p=[[3,0]]

    visited = [None] * n
    for i in range(n):
        if dfs(graph, visited, i):
            print ("true"); return
    print("false"); return
        
def dfs(graph, visited, i):
    if visited[i] == 1: return True #1 = visiting
    if visited[i] == 2: return False  #2 = visited
    visited[i] = 1
    print(visited)
    for j in graph[i]:
        print(j)
        if dfs(graph, visited, j):
            print("forloop", visited)
            return True
    visited[i] = 2
    print("endforloop",visited)
    return False
    
    
        
