# boj 11370 Spawn of Ungoliant
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 'T':
                graph[nx][ny] = 'S'
                queue.append((nx, ny))


while True:
    m, n = map(int, input().split())
    if (m, n) == (0, 0):
        break
    graph = []

    for _ in range(n):
        graph.append(list(input()))

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'S':
                bfs(i, j)

    for i in range(n):
        for j in range(m):
            print(graph[i][j], end='')
        print()