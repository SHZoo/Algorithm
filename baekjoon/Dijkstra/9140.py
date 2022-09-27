# boj 9140 Přeprava materiálu
import heapq

INF = (1e11)

def dijkstra(start):
    hq = []
    heapq.heappush(hq, (0, start))

    while hq:
        dist, now = heapq.heappop(hq)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(hq, (cost, i[0]))

while True:
    n, m, start, destination = map(int, input().split())
    if (n, m, start, destination) == (0, 0, 0, 0): break
    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)

    for _ in range(m):
        u, v, c = map(int, input().split())
        graph[u].append((v, c))
    if start == destination:
        print(0)
    else:
        dijkstra(start)
        print(distance[destination])
