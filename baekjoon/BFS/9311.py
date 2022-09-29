# boj 9311 Robot in a Maze
from collections import deque

t = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    queue = deque([(x, y)])
    graph[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 'O' or graph[nx][ny] == '0':
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
            elif graph[nx][ny] == 'G':
                return graph[x][y]
    return None

for i in range(t):
    n, m = map(int, input().split())
    graph = []

    for i in range(n):
        input_data = list(input())
        for j in range(m):
            if input_data[j] == 'S':
                x, y = i, j
        graph.append(input_data)
    
    res = bfs(x, y)
    if res == None:
        print('No Exit')
    else:
        print("Shortest Path: {}".format(res))
