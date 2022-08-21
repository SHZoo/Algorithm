# boj 10568 Wormholes
import math

t = int(input())
INF = (1e10)

for test_case in range(1, t+1) :
    dict = {}
    n = int(input())
    graph = [[INF]*n for _ in range(n)]
    array = []
    
    for i in range(n) :
        for j in range(n) :
            if i == j :
                graph[i][j] = 0

    for i in range(n) :
        input_data = input().split()
        dict[input_data[0]] = i
        array.append((int(input_data[1]), int(input_data[2]), int(input_data[3])))
    
    for i in range(n-1) :
        for j in range(i+1, n) :
            dist = math.sqrt((array[i][0]-array[j][0])**2 + (array[i][1]-array[j][1])**2 + (array[i][2]-array[j][2])**2)
            graph[i][j] = dist
            graph[j][i] = dist

    m = int(input())

    for _ in range(m) :
        input_data = input().split()
        graph[dict[input_data[0]]][dict[input_data[1]]] = 0

    for k in range(n) :
        for i in range(n) :
            for j in range(n) :
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    
    c = int(input())
    print("Case {}:".format(test_case))
    for _ in range(c) :
        input_data = input().split()
        print("The distance from {} to {} is {} parsecs.".format(input_data[0], input_data[1], int(graph[dict[input_data[0]]][dict[input_data[1]]] + 0.5)))