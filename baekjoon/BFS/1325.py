# boj 1325 효율적인 해킹
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[v].append(u)

def bfs(start):
    queue = deque([start])
    visited[start] = True
    sum = 0
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                sum += 1
                queue.append(i)

    return sum
res_list = []
max_com = -1

for i in range(1, n+1):
    visited = [False] * (n+1)
    res = bfs(i)
    if res > max_com:
        max_com = res
        res_list.clear()
        res_list.append(i)
    elif res == max_com:
        res_list.append(i)

print(*res_list)