# boj 2468
import sys
import copy
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
graph_copy = []
min_height = 0
max_height = 0
for i in range(n) :
    input_data = list(map(int, input().split()))
    graph_copy.append(input_data)
    min_height = min(min_height, min(input_data))
    max_height = max(max_height, max(input_data))
graph = copy.deepcopy(graph_copy)
def dfs(x, y, height) :
    if x < 0 or y < 0 or x >= n or y >= n :
        return False
    if graph[x][y] > height :
        graph[x][y] = height
        dfs(x+1, y, height)
        dfs(x-1, y, height)
        dfs(x, y+1, height)
        dfs(x, y-1, height)
        return True
    return False

res = 0
for k in range(min_height, max_height+1) :
    max_region = 0
    for i in range(n) :
        for j in range(n) :
            if dfs(i, j, k) == True :
                max_region += 1
    res = max(res, max_region)
    graph = copy.deepcopy(graph_copy)

print(res)