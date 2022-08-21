# boj 3075 Astromeeting
t = int(input())
INF = (1e11)
for _ in range(t) :
    n, p, q = map(int, input().split())
    max_cost = INF
    res_node = 0
    graph = [[INF] * (p+1) for _ in range(p+1)]
    array = []
    
    for _ in range(n) :
        array.append((int(input())))

    for i in range(1, p+1) :
        for j in range(1, p+1) :
            if i == j :
                graph[i][j] = 0

    for _ in range(q) :
        u, v, c = map(int, input().split())
        graph[u][v] = min(graph[u][v], c)
        graph[v][u] = min(graph[v][u], c)
    
    for k in range(1, p+1) :
        for i in range(1, p+1) :
            for j in range(1, p+1) :
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    
    for i in range(1, p+1) :
        sum = 0
        for friend in array :
            sum += graph[friend][i] ** 2
        if sum < max_cost :
            max_cost = sum
            res_node = i

    print(res_node, max_cost)