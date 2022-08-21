# boj 6598 Arbitrage
INF = (1e10)
s = 0
while True :
    s += 1
    n = int(input())
    if n == 0 : break
    dict = {}
    graph = [[0]*n for _ in range(n)]
    for i in range(n) :
        for j in range(n) :
            if i == j :
                graph[i][j] = 0

    for i in range(n) :
        dict[input()] = i
    
    m = int(input())

    for _ in range(m) :
        input_data = input().split()
        graph[dict[input_data[0]]][dict[input_data[2]]] = float(input_data[1])

    for k in range(n) :
        for i in range(n) :
            for j in range(n) :
                graph[i][j] = max(graph[i][j], graph[i][k] * graph[k][j])

    if graph[0][0] > 1 :
        print('Case {}: Yes'.format(s))
    else :
        print('Case {}: No'.format(s))
    
    input()