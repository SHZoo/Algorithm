# boj 25416 빠른 숫자 탐색
from collections import deque

graph = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(5):
    graph.append(list(map(int, input().split())))

start_x, start_y = map(int, input().split())

def bfs(x, y):
    queue = deque([(x, y)])
    if graph[x][y] == 1:
        return 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= 5 or ny >= 5:
                continue
            if graph[nx][ny] == 1:
                return graph[x][y] - 1
            elif graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] - 1
                queue.append((nx, ny))

res = bfs(start_x, start_y)

if res == None:
    print(-1)
else:
    print(-res)