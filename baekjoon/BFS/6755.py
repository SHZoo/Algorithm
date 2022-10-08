# boj 6755 Who is taller?/pypy로 제출할 것
from collections import deque

n, m = map(int, input().split())
graph_1 = [[] for _ in range(n+1)]
graph_2 = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(m):
    u, v = map(int, input().split())
    graph_1[u].append(v)
    graph_2[v].append(u)

def bfs_1(start, graph, visited, destination):
    queue = deque([start])
    visited[start] = True
    while queue:
        now = queue.popleft()
        if now == destination:
            return 'yes'
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

def bfs_2(start, graph, visited, destination):
    queue = deque([start])
    visited[start] = True
    while queue:
        now = queue.popleft()
        if now == destination:
            return 'no'
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

start, destination = map(int, input().split())

res = bfs_1(start, graph_1, visited, destination)
if res == 'yes':
    print(res)
else:
    visited = [False] * (n+1)
    res = bfs_2(start, graph_2, visited, destination)
    if res == 'no':
        print(res)
    else:
        print('unknown')
