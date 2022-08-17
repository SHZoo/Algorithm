# boj 3055 탈출
from collections import deque

n, m = map(int, input().split())
water_list = []
graph = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(n) :
    input_data = list(input())
    for j in range(m) :
        if input_data[j] == '*' :
            water_list.append((i, j, 1))
        if input_data[j] == 'S' :
            s_list = (i, j, 0)
    graph.append(input_data)
queue = deque(water_list)
queue.append(s_list) 
graph[s_list[0]][s_list[1]] = 0
def bfs() :
    while queue :
        x, y, state = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m :
                continue
            if state == 0 :
                if graph[nx][ny] == '.' :
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny, 0))
                elif graph[nx][ny] == 'D' :
                    return graph[x][y] + 1
            if state == 1 :
                if graph[nx][ny] == '.' :
                    graph[nx][ny] = '*'
                    queue.append((nx, ny, 1))
    return 'KAKTUS'
            
print(bfs())