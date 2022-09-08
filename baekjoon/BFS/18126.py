# boj 18126 너구리 구구
from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(n-1):
    u, v, c = map(int, input().split())
    graph[u].append((v, c))
    graph[v].append((u, c))

def bfs():
    queue = deque([(1, 0)])
    max_dist = 0
    while queue:
        now, dist = queue.popleft()
        max_dist = max(max_dist, dist)
        visited[now] = True
        for i in graph[now]:
            if not  visited[i[0]]:
                visited[i[0]] = True
                queue.append((i[0], dist+i[1]))

    return max_dist

print(bfs())