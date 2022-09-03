# boj 17086 아기상어2
from collections import deque

n, m = map(int, input().split())
graph = []
queue = deque()
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, 1, 1, -1, -1]
for i in range(n):
    input_data = list(map(int, input().split()))
    for j in range(m):
        if input_data[j] == 1:
            queue.append((i, j))
    graph.append(input_data)

def bfs():
    max_dist = 0
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or ny < 0 or nx >=n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx, ny))
    for i in range(n):
        for j in range(m):
            max_dist = max(max_dist, graph[i][j])
    return max_dist-1

print(bfs())
