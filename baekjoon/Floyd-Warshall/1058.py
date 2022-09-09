# boj 1058 친구
n = int(input())
INF = (1e10)
graph = [[INF] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            graph[i][j] = 0

for i in range(n):
    input_data = list(input())
    for j in range(n):
        if input_data[j] == 'Y':
            graph[i][j] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

max_dist = 0
for i in range(n):
    sum_friend = 0
    for j in range(n):
        if graph[i][j] == 1 or graph[i][j] == 2:
            sum_friend += 1
    max_dist = max(max_dist, sum_friend)

print(max_dist)