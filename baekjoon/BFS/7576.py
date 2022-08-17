# boj 7576
from collections import deque

m, n = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
graph = []
tomato_list = []
for i in range(n) :
    input_data = list(map(int, input().split()))
    for j in range(m) :
        if input_data[j] == 1 :
            tomato_list.append((i, j))
    graph.append(input_data)

queue = deque(tomato_list)
def bfs() :
    max_day = 0
    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m :
                continue
            if graph[nx][ny] == 0 :
                graph[nx][ny] = graph[x][y] + 1 
                queue.append((nx, ny))
    for i in range(n) :
        for j in range(m) :
            if graph[i][j] == 0 :
                return -1
            max_day = max(max_day, graph[i][j])

    return max_day - 1

print(bfs())