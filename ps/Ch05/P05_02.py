from collections import deque 
import sys
n, m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n) :
    graph.append(list(map(int, sys.stdin.readline().strip())))

# 반복문으로 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y) :
    queue = deque([(x, y)])
    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx <= -1 or ny <= -1 or ny >= m or nx >= n :
                continue
            if graph[nx][ny] == 0 :
                continue
            if graph[nx][ny] == 1 :
                graph[nx][ny] = graph[x][y] +1
                queue.append((nx,ny))
    return  graph[n-1][m-1]

print(bfs(0,0))
