# boj 9303 Hoo's Afraid of the Big Bad Wolf?
import heapq 

t = int(input())
INF = (1e9)

for i in range(1, t+1) :
    n = int(input())
    start, destination = map(int, input().split())
    m = int(input())
    graph = [[] for _ in range(n+1)]
    distance = [0] * (n+1)

    for _ in range(m) :
        u, v, c = map(float, input().split())
        graph[int(u)].append((int(v), c))
        #graph[int(v)].append((int(u), c))

    def dijkstra(start) :
        hq = []
        heapq.heappush(hq, (1, start))
        distance[start] = 1

        while hq :
            prob, now = heapq.heappop(hq)
            if distance[now] > prob :
                continue
            for i in graph[now] :
                cost = prob * i[1]
                if distance[i[0]] < cost :
                    distance[i[0]] = cost
                    heapq.heappush(hq, (cost, i[0]))

    dijkstra(start)
    print("Case {}: {:.4f}".format(i, distance[destination]))