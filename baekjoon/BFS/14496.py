# boj 14496 그대, 그머가 되어
from collections import deque

start, destination = map(int, input().split())
n, m = map(int, input().split())
visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(start):
    queue = deque([(start, 0)])
    visited[start] = True
    while queue:
        now, cnt = queue.popleft()
        if now == destination:
            return cnt
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                queue.append((i, cnt+1))

    return None

res = bfs(start)
if res == None:
    print(-1)
else:
    print(res)