# boj 11403 경로 찾기
n = int(input())
INF = 1e9
graph = [[INF]*(n) for _ in range(n)]

for i in range(n):
    input_data = list(map(int, input().split()))
    for j in range(n):
        if input_data[j] == 1:
            graph[i][j] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            print(0, end = ' ')
        else:
            print(1, end = ' ')
    print()