# boj 6528 106 miles to Chicago
import heapq

def dijkstra(start):
    hq = []
    heapq.heappush(hq, (1, start))
    distance[start] = 1
    while hq:
        dist, now = heapq.heappop(hq)
        if distance[now] > dist:
            continue
        for i in graph[now]:
            cost = dist * (i[1]*0.01)
            if distance[i[0]] < cost:
                distance[i[0]] = cost
                heapq.heappush(hq, (cost, i[0]))

while True:
    try:
        n, m = map(int, input().split())
        graph = [[] for _ in range(n+1)]
        distance = [0] * (n+1)

        for _ in range(m):
            u, v, p = map(int, input().split())
            graph[u].append((v, p))
            graph[v].append((u, p))

        dijkstra(1)
        print("{:.6f} percent".format(round(distance[n]*100, 6)))

    except:
        break
