# boj 14502
from itertools import combinations
from collections import deque
import sys
import copy
input = sys.stdin.readline

graph = []
virus_list = []
vacuum_list = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
n, m = map(int, input().split())

for i in range(n) :
    input_data = list(map(int, input().split()))
    graph.append(input_data)
    for j in range(len(input_data)) :
        if input_data[j] == 0 :
            vacuum_list.append((i, j))
        elif input_data[j] == 2 :
            virus_list.append((i, j))

wall_list = list(combinations(vacuum_list, 3))


def bfs(graph) :
    res = 0
    queue = deque(virus_list)
    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m :
                continue
            if graph[nx][ny] == 0 :
                graph[nx][ny] = 2
                queue.append((nx, ny))

    for i in range(n) :
        for j in range(m) :
            if graph[i][j] == 0 :
                res += 1    
    return res
max_res = 0
graph_copy = copy.deepcopy(graph)
for wall in wall_list :
    for w in wall :
        u, v = w
        graph_copy[u][v] = 1
    max_res = max(max_res, bfs(graph_copy))
    graph_copy = copy.deepcopy(graph)
    
print(max_res)