# boj 2583 영역 구하기
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m, k = map(int, input().split())
graph = [[1]*(m) for _ in range(n)]

for _ in  range(k) :
    x1, y1, x2, y2 = map(int,input().split())
    for i in range(n-y2, n-y1) :
        for j in range(x1, x2) :
            graph[i][j] = 0

def dfs(x, y) :
    global res
    if x < 0 or y < 0 or x >= n or y >= m :
        return False
    if graph[x][y] == 1 :
        res += 1
        graph[x][y] = 0
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return res
    return False
array = []
for i in range(n) :
    for j in range(m) :
        res = 0
        result = dfs(i, j)
        if result != 0 :
            array.append(result)

array.sort()
print(len(array))
print(*array)