# boj 24446 알고리즘 수업-너비 우선 탐색3
from collections import deque

n, m, start = map(int, input().split())
INF = (1e9)
graph = [[]for _ in range(n+1)]
visited = [INF] * (n+1)
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(start):
    queue = deque([(start, 0)])
    visited[start] = 0
    while queue:
        now, cnt = queue.popleft()

        for i in graph[now]:
            if visited[i] == INF:
                visited[i] = min(visited[i], cnt+1)
                queue.append((i, cnt+1))
bfs(start)

for i in range(1, n+1):
    if visited[i] == INF:
        print(-1)
    else:
        print(visited[i])