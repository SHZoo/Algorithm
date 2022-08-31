# boj 6118 숨바꼭질
from collections import deque
import sys

input = sys.stdin.readline
n, m  = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [-1] * (n+1)
visited = [False] * (n+1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(start):
    queue = deque()
    visited[start] = True
    queue.append((start, 0))
    distance[start] = 0
    res_list = []
    while queue:
        now, cnt = queue.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                distance[i] = cnt+1
                queue.append((i, cnt+1))
    max_cnt = max(distance)
    for i in range(1, n+1):
        if distance[i] == max_cnt:
            res_list.append(i)
    print(res_list[0], max_cnt, len(res_list))

bfs(1)