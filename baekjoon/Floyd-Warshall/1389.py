# 1389 케빈 베이컨의 6단계 법칙
n, m = map(int, input().split())
INF = (1e10)
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1) :
    for j in range(1, n+1) :
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    u, v = map(int, input().split())
    graph[u][v] = 1
    graph[v][u] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

Kevin_Bacon = INF
res_list = []

for i in range(1, n+1):
    if sum(graph[i][1:]) < Kevin_Bacon:
        res_list.clear()
        res_list.append(i)
        Kevin_Bacon = sum(graph[i][1:])
    elif sum(graph[i][1:]) == Kevin_Bacon:
        res_list.append(i)

res_list.sort()
print(res_list[0])