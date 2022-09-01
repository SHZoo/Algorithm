# boj 14716 현수막
from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, 1, -1, -1, 1]
res = 0

for _ in range(n):
    graph.append(list(map(int, input().split())))


def bfs(x, y):
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            res += 1
            bfs(i, j)

print(res)