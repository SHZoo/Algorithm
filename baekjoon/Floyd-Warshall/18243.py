# boj 18243 Small World Network
import sys

input = sys.stdin.readline
INF = (1e9)
n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(n+1):
    for j in range(n+1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    u, v = map(int, input().split())
    graph[u][v] = 1
    graph[v][u] = 1

for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

max_realation = 0

for i in range(1, n+1):
    max_realation = max(max_realation, max(graph[i][1:]))

if max_realation <= 6:
    print('Small World!')
else:
    print('Big World!')