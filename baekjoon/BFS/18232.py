# boj 18232 텔레포트 정거장
from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
start, destination = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(start, destination):
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

        if now+1 <= n and not visited[now+1]:
            visited[now+1] = True
            queue.append((now+1, cnt+1))
        if now-1 >= 0 and not visited[now-1]:
            visited[now-1] = True
            queue.append((now-1, cnt+1))

print(bfs(start, destination))