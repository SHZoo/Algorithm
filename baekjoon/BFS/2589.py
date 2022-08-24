# boj 2589 보물섬
from collections import deque
import heapq
import sys
import copy
input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
hq = []
for _ in range(n) :
    graph.append(list(input().strip()))

graph_copy = copy.deepcopy(graph)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y, graph) :
    queue = deque([])
    queue.append((x, y))
    graph[x][y] = 0
    max_distance = 0
    while queue :
        x, y = queue.popleft()
        
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m :
                continue
            if graph[nx][ny] == 'W' :
                continue
            if graph[nx][ny] == 'L' :
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
                max_distance = max(max_distance, graph[nx][ny])
    return max_distance
    
for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 'W' :
            continue
        elif graph[i][j] == 'L' :
            heapq.heappush(hq, -bfs(i, j, graph_copy))
            
            graph_copy = copy.deepcopy(graph)
            
print(-heapq.heappop(hq)) 