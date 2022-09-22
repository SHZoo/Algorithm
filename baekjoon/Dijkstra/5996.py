# boj 5996 Heat Wave
import heapq

INF = (1e10)
n, m, start, end = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    u, v, c= map(int, input().split())
    graph[u].append((v, c))
    graph[v].append((u, c))

def dijkstra(start):
    hq = []
    heapq.heappush(hq, (0, start))
    distance[start] = 0

    while hq:
        dist, now = heapq.heappop(hq)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(hq, (cost, i[0]))

dijkstra(start)
print(distance[end])
