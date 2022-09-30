# boj 1388 바닥장식
from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(input()))
d = [1, -1]


def bfs(x, y):
    queue = deque([(x, y)])
    if graph[x][y] == '-':
        graph[x][y] = 0
    if graph[x][y] == '|':
        graph[x][y] = 1
    while queue:
        x, y = queue.popleft()
        if graph[x][y] == 0:
            for i in range(2):
                ny = y+d[i]
                if ny < 0 or ny >= m:
                    continue
                if graph[x][ny] == '-':
                    graph[x][ny] = 0
                    queue.append((x, ny))
        elif graph[x][y] == 1:
             for i in range(2):
                nx = x+d[i]
                if nx < 0 or nx >= n:
                    continue
                if graph[nx][y] == '|':
                    graph[nx][y] = 1
                    queue.append((nx, y))

res = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == '-' or graph[i][j] == '|':
            res += 1
            bfs(i, j)

print(res)
