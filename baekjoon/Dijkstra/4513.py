# boj 4513 The Neptune Adventure
import heapq 

t = int(input())
INF = (1e10)
for _ in range(t) :
    n, start, destination = map(int, input().split())
    time = [0]
    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)

    for i in range(1, n+1) :
        input_data = list(map(int, input().split()))
        time.append(input_data[0])

        for j in range(1, n+1) :
            if input_data[j] == 0 :
                continue
            graph[i].append((j, input_data[j]))
        
    def dijkstra(start) :
        hq = []
        heapq.heappush(hq, (0, start))
        distance[start] = 0

        while hq :
            dist, now = heapq.heappop(hq)
            if distance[now] < dist :
                continue
            for i in graph[now] :
                cost = dist + i[1]
                if time[now] != 0 and time[now] < cost :
                    continue
                if time[i[0]] != 0 and time[i[0]] < cost :
                    continue
                if distance[i[0]] > cost :
                    distance[i[0]] = cost
                    heapq.heappush(hq, (cost, i[0]))

    dijkstra(start)
    if distance[destination] >= INF :
        print('GENE HACKMAN')
    else :
        print(distance[destination])
    