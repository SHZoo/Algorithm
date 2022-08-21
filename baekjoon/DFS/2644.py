# boj 2644 촌수계산
from collections import deque

n = int(input())
start, destination = map(int, input().split())
graph = [[] for _ in range(n+1)]
m = int(input())
visited = [False] * (n+1)
for _ in range(m) :
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(graph, start, visited, destination) :
    queue = deque([(start, 0)])
    
    while queue :
        now, dist = queue.popleft()
        if now == destination :
            return dist
        visited[now] = True 
        for i in graph[now] :
            if not visited[i] :
                visited[i] = True
                queue.append((i, dist+1))
    return -1

print(bfs(graph, start, visited, destination))