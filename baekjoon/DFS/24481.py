# boj 24481 알고리즘 수업 - 깊이 우선 탐색 3
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = (1e9)
n, m, start = map(int, input().split())
visited = [INF] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(start, k):
    visited[start] = min(visited[start], k)
    graph[start].sort()
    for i in graph[start]:
        if visited[i] == INF:
            dfs(i, k+1)

dfs(start, 0)

for i in range(1, n+1):
    if visited[i] == INF:
        print(-1)
    else:
        print(visited[i])