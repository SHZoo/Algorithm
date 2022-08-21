# boj 6595 프로거/ pypy로 제출해야 함 
import math

INF = 1e11
l = 0
while True :
    l += 1
    n = int(input())
    max_distance = 0 
    if n == 0 : 
        break
    array = []

    for _ in range(n) :
        u, v = map(int, input().split())
        array.append((u, v))

    graph = [[INF] * n for _ in range(n)]

    for i in range(n) :
        for j in range(n) :
            if i == j :
                graph[i][j] = 0

    for i in range(n-1) :
        for j in range(i+1, n) :
            dist = math.sqrt((array[i][0] - array[j][0]) ** 2 + (array[i][1] - array[j][1]) ** 2)
            graph[i][j] = dist
            graph[j][i] = dist 

    for k in range(n) :
        for i in range(n) :
            for j in range(n) :
                if i == k or j == k:
                    continue
                graph[i][j] = min(graph[i][j], max(graph[i][k], graph[k][j]))


    max_distance = graph[0][1]

    print("Scenario #{}".format(l))
    print("Frog Distance = {:.3f}".format(round(max_distance, 3)))
    print()
    input() # 테스트 케이스에 공백 행이 있음