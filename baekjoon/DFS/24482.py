# boj 24482 알고리즘 수업 - 깊이 우선 탐색 4
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, start = map(int, input().split())
graph = [[] for _ in range(n+1)]
INF = (1e9)
visited = [INF] * (n+1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(start, cnt):
    visited[start] = min(visited[start], cnt)
    graph[start].sort(reverse = True)

    for i in graph[start]:
        if visited[i] == INF:
            dfs(i, cnt+1)
dfs(start, 0)
for i in range(1, n+1):
    if visited[i] == INF:
        print(-1)
    else:
        print(visited[i])