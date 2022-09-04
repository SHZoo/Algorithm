# boj 21736 헌내기는 친구가 필요해
from collections import deque

n, m = map(int, input().split())
graph = []
queue = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(n):
    input_data = list(input())
    graph.append(input_data)
    for j in range(m):
        if input_data[j] == 'I':
            queue.append((i, j))

def bfs():
    friend = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 'O':
                graph[nx][ny] = 0
                queue.append((nx, ny))
            elif graph[nx][ny] == 'P':
                graph[nx][ny] = 0
                friend += 1
                queue.append((nx, ny))
    return friend

res = bfs()
if not res:
    print('TT')
else:
    print(res)