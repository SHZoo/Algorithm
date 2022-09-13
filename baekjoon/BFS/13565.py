# boj 13565 침투
from collections import deque

n, m = map(int, input().split())
graph = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(n):
    graph.append(list(map(int, input())))

def bfs(x, y):
    queue = deque([(x, y)])
    graph[x][y] = 2

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                queue.append((nx, ny))
res = 'NO'

for i in range(m):
    if graph[0][i] == 0:
        bfs(0, i)

for i in range(m):
    if graph[n-1][i] == 2:
        res = 'YES'
        break

print(res)