# boj 17270 연예인은 힘들어
import sys
input = sys.stdin.readline
INF = (1e9)

n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1) :
    for j in range(1, n+1) :
        if i == j :
            graph[i][j] = 0

for _ in range(m) :
    u, v, c = map(int, input().split())
    graph[u][v] = min(graph[u][v], c)
    graph[v][u] = min(graph[u][v], c)

for k in range(1, n+1) :
    for i in range(1, n+1) :
        for j in range(1, n+1) :
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

x, y = map(int, input().split())
max_time = INF
res_list = []
for i in range(1, n+1) :
    if i == x or i == y :
        continue
    if max_time > (graph[x][i] + graph[y][i]) :
        res_list.clear()
        res_list.append((graph[x][i], i))
        max_time = graph[x][i] + graph[y][i]
    elif max_time == (graph[x][i] + graph[y][i]) :
        res_list.append((graph[x][i], i))

if len(res_list) == 0 :
    print(-1)
else :
    res_list = sorted(res_list, key = lambda res_list : (res_list[0], res_list[1]))
    for i in range(len(res_list)) :
        if graph[x][res_list[i][1]] > graph[y][res_list[i][1]] :
             pass
        else :
            print(res_list[i][1])
            break
        if i == len(res_list) -1 :
            print(-1) 
