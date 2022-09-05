# boj 14940 쉬운 최단거리
from collections import deque

n, m = map(int, input().split())
graph = []
queue = deque()
dict = {}
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(n):
    input_data = list(map(int, input().split()))
    for j in range(len(input_data)):
        if input_data[j] == 2:
            input_data[j] = 0
            queue.append((i, j))
        if input_data[j] == 1:
            input_data[j] = -1
    graph.append(input_data)

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == -1 and (nx, ny) not in dict:
                dict[(nx, ny)] = 0
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

bfs()
for i in graph:
    print(*i)