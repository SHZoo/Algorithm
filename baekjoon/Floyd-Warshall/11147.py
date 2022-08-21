# boj 11147 Travelling Tom/ pypy로 제출할 것
t = int(input())
INF = (1e9)

for _ in range(t) :
    n = int(input())
    sum = 0
    graph = [[INF] * (n) for _ in range(n)]
    for i in range(n) :
        for j in range(n) :
            if i == j :
                graph[i][j] = 0
    array = list(map(int, input().split()))
    tour_list = []
    for i in range(len(array)) :
        if i == len(array) -1 :
            tour_list.append((array[-1], array[0]))
        else :
            tour_list.append((array[i], array[i+1]))

    for i in range(n) :
        input_data = list(map(int, input().split()))
        for j in range(n) :
            if input_data[j] == -1 :
                continue
            graph[i][j] = min(graph[i][j], input_data[j])

    for k in range(n) :
        for i in range(n) :
            for j in range(n) :
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    for tour in tour_list :
        u, v = tour 
        sum += graph[u][v]
    
    if sum >= INF :
        print('impossible')
    else :
        print(sum)