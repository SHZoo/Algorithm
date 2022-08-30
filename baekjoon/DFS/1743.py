# boj 1743 음식물 피하기
import sys

sys.setrecursionlimit(10**6)
n, m, k = map(int, input().split())
graph = [[0]*(m) for _ in range(n)]
max_res = 0

for _ in range(k):
    u, v = map(int, input().split())
    graph[u-1][v-1] = 1

def dfs(x, y):
    global  res
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        res += 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

for i in range(n):
    for j in range(m):
        res = 0
        dfs(i, j)
        max_res = max(max_res, res)

print(max_res)