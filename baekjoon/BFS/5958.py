# boj 5958 Space Exploration
from collections import deque

n = int(input())
graph = []
res = 0
num = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for _ in range(n):
    graph.append(list(input()))

def bfs():
    global num
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] == '*':
                graph[nx][ny] = num
                queue.append((nx, ny))

for i in range(n):
    for j in range(n):
        if graph[i][j] == '*':
            num += 1
            queue = deque([(i, j)])
            bfs()

print(num)