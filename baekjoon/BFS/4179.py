# boj 4179 불!
from collections import deque

n, m = map(int, input().split())
visited = [[[0, 0] for _ in range(m)] for _ in range(n)]
graph = []
queue = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(n):
    input_data = input()
    for j in range(m):
        if input_data[j] == 'F':
            queue.append((0, i, j))
        elif input_data[j] == 'J':
            queue.append((1, i, j))
    graph.append(input_data)
queue.sort()
queue = deque(queue)
def bfs():
    while queue:
        state, x, y = queue.popleft()
        if state == 0: # 불이라면
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if graph[nx][ny] == '.' and visited[nx][ny][1] == 0:
                    visited[nx][ny][1] = 1
                    queue.append((0, nx, ny))
        if state == 1: # 지훈이라면
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    return visited[x][y][0]+1
                if graph[nx][ny] == '.' and visited[nx][ny][1] != 1 and visited[nx][ny][0] == 0:
                    visited[nx][ny][0] = visited[x][y][0] + 1
                    queue.append((1, nx, ny))
    return None
res = bfs()
if res == None:
    print('IMPOSSIBLE')
else :
    print(res)