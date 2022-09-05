# boj 1303 전쟁 - 전투
m, n = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(input()))

def dfs_W(x, y):
    global res_w
    if x < 0 or y < 0 or x >= n or y >= m:
        return
    if graph[x][y] == 'W':
        res_w += 1
        graph[x][y] = 0
        dfs_W(x+1, y)
        dfs_W(x-1, y)
        dfs_W(x, y+1)
        dfs_W(x, y-1)
        return
    return

def dfs_B(x, y):
    global res_b
    if x < 0 or y < 0 or x >= n or y >= m:
        return
    if graph[x][y] == 'B':
        res_b += 1
        graph[x][y] = 0
        dfs_B(x+1, y)
        dfs_B(x-1, y)
        dfs_B(x, y+1)
        dfs_B(x, y-1)
        return
    return

res_list_1 = []
res_list_2 = []

for i in range(n):
    for j in range(m):
        res_b = 0
        dfs_B(i, j)
        res_w = 0
        dfs_W(i, j)
        if res_b > 0:
            res_list_1.append(res_b)
        if res_w > 0:
            res_list_2.append(res_w)

res_list_1 = list(res_list_1)
res_list_2 = list(res_list_2)
sum_1 = 0
sum_2 = 0
for i in res_list_1:
    sum_1 += i**2
for j in res_list_2:
    sum_2 += j**2

print(sum_2, sum_1)