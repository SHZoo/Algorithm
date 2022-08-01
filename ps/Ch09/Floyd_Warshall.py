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
    u, v, w = map(int, input().split())
    graph[u][v] = w
 
for k in range(1, n+1) :
    for i in range(1, n+1) :
        for j in range(1, n+1) :
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n+1) :
    for j in range(1, n+1) :
        if graph[i][j] == INF :
            print('INFINITY', end = ' ')
        else :
            print(graph[i][j], end = ' ')
    print() # 줄넘김