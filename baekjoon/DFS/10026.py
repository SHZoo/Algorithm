# boj 10026
import sys
import copy
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
graph_copy = []
n = int(input())
for _ in range(n) :
    graph_copy.append(list(input().strip()))
graph = copy.deepcopy(graph_copy)
def dfs_1(x, y) :
    if x < 0 or y < 0 or x >= n or y >= n :
        return False
    if graph[x][y] == 'R' :
        graph[x][y] = 1
        dfs_1(x+1,y)
        dfs_1(x-1,y)
        dfs_1(x,y+1)
        dfs_1(x,y-1)
        return True
    return False

def dfs_2(x, y) :
    if x < 0 or y < 0 or x >= n or y >= n :
        return False
    if graph[x][y] == 'G' :
        graph[x][y] = 1
        dfs_2(x+1,y)
        dfs_2(x-1,y)
        dfs_2(x,y+1)
        dfs_2(x,y-1)
        return True
    return False

def dfs_3(x, y) :
    if x < 0 or y < 0 or x >= n or y >= n :
        return False
    if graph[x][y] == 'B' :
        graph[x][y] = 1
        dfs_3(x+1,y)
        dfs_3(x-1,y)
        dfs_3(x,y+1)
        dfs_3(x,y-1)
        return True
    return False

def dfs_4(x, y) :
    if x < 0 or y < 0 or x >= n or y >= n :
        return False
    if graph[x][y] == 'R' or graph[x][y] == 'G' :
        graph[x][y] = 1
        dfs_4(x+1,y)
        dfs_4(x-1,y)
        dfs_4(x,y+1)
        dfs_4(x,y-1)
        return True
    return False

res_1 = 0
res_2 = 0
for i in range(n) :
    for j in range(n) :
        if dfs_1(i, j) or dfs_2(i, j) or dfs_3(i, j) ==  True :
            res_1 += 1
graph = copy.deepcopy(graph_copy)
for i in range(n) :
    for j in range(n) :
        if dfs_3(i, j) or dfs_4(i, j) == True :
            res_2 += 1
print(res_1, res_2)