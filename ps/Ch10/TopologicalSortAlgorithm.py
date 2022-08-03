# Topological Sort Algorithm
# 전제 조건 : 방향 비순환 그래프(DAG)
from collections import deque
from gc import garbage

v, e = map(int, input().split())

indegree = [0] * (v+1)
graph = [[] for _ in range(v+1)]

for _ in range(e) :
    u, v = map(int, input().split())
    graph[u].append(v)
    indegree[v] += 1

def topology_sort() :
    result = []
    queue = deque()

    for i in range(1, v+1) :
        if indegree[i] == 0 :
            queue.append(i)
    
    while queue :
        now = queue.popleft()
        result.append(now)

        for i in graph[now] :
            indegree[i] -= 1 
            if indegree[i] == 0 :
                queue.append(i)
        
    for i in result :
        print(i, end = ' ')
    
topology_sort()