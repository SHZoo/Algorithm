# boj 18780 Timeline 
from collections import deque
import copy

n, m, c = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
time = [0]
time.extend(list(map(int, input().split())))

for _ in range(c) :
    u, v, q = map(int, input().split())
    graph[u].append((v, q))
    indegree[v] += 1

def topology_sort() :
    queue = deque()
    result = copy.deepcopy(time)
    for i in range(1, n+1) :
        if indegree[i] == 0 :
            queue.append(i)
    
    while queue :
        now = queue.popleft()
        for i in graph[now] :
            indegree[i[0]] -= 1
            result[i[0]] = max(result[i[0]], result[now] + i[1])
            if indegree[i[0]] == 0 :
                queue.append(i[0])
    
    return result[1:n+1]

print(*topology_sort(), sep = '\n')
