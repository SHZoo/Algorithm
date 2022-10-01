# boj 4993 Red and Black
import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    global res
    if x < 0 or x >= n or y < 0 or y >= m:
        return
    if graph[x][y] == '.' or graph[x][y] == '@':
        res += 1
        graph[x][y] = 0
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return
    return

while True:
    m, n = map(int, input().split())
    if (m, n) == (0, 0): break
    graph = []
    res = 0
    for i in range(n):
        input_data = list(input())
        for j in range(m):
            if input_data[j] == '@':
                (x, y) = (i, j)
        graph.append(input_data)

    dfs(x, y)
    print(res)
