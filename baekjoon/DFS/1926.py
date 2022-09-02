# boj 1926 그림
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
res_list = []
n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

def dfs(x, y):
    global res
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    if graph[x][y] == 1:
        res += 1
        graph[x][y] = 0
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True
    return False

for i in range(n):
    for j in range(m):
        res = 0
        dfs(i, j)
        if res != 0:
            res_list.append(res)

if len(res_list) == 0:
    print(0, 0, sep = '\n')
else:
    print(len(res_list), max(res_list), sep = '\n')