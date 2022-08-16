# boj 2206
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n) :
    for j in range(m) :
        graph[i][j] = [graph[i][j], 0, 0]

def bfs() :
    queue = deque([(0, 0, 0)])
    if (n-1, m-1) == (0, 0) :
        return 1
    while queue :
        x, y, state = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m :
                continue
            if state == 0 :
                if graph[nx][ny][0] == 0 :
                    if graph[nx][ny][1] == 0 :
                        graph[nx][ny][1] += graph[x][y][1] + 1
                        queue.append((nx, ny, 0))
                    if (nx, ny) == (n-1, m-1) :
                        return graph[nx][ny][1] + 1
                elif graph[nx][ny][0] == 1 :
                    if graph[nx][ny][2] == 0 :
                        graph[nx][ny][2] += graph[x][y][1] + 1
                        queue.append((nx, ny, 1))
            elif state == 1 :
                if graph[nx][ny][0] == 0 :
                    if graph[nx][ny][2] == 0 :
                        graph[nx][ny][2] += graph[x][y][2] + 1
                        queue.append((nx, ny, 1))
                    if (nx, ny) == (n-1, m-1) :
                        return graph[nx][ny][2] + 1
    return -1

print(bfs())
