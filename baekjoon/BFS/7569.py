# boj 7569
from collections import deque

m, n, t = map(int, input().split())
graph = [[] for _ in range(t)]
tomato_list = []
for i in range(t) :
    for j in range(n) :
        input_data = list(map(int, input().split()))
        for k in range(m) :
            if input_data[k] == 1 :
                tomato_list.append((i, j, k))
        graph[i].append(input_data)

dz = [1, -1, 0, 0, 0, 0]
dx = [0, 0, 1, -1, 0, 0]
dy = [0, 0, 0, 0, 1, -1]

queue = deque(tomato_list)

def bfs() :
    max_day = 0
    while queue :
        z, x, y = queue.popleft()
        for i in range(6) :
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]
            if nx < 0 or ny < 0 or nz < 0 or nx >= n or ny >= m or nz >= t :
                continue
            if graph[nz][nx][ny] == 0 :
                graph[nz][nx][ny] = graph[z][x][y] + 1
                queue.append((nz, nx, ny))
    for i in range(t) :
        for j in range(n) :
            for k in range(m) :
                if graph[i][j][k] == 0 :
                    return -1
                max_day = max(max_day, graph[i][j][k])

    return max_day - 1

print(bfs()) 