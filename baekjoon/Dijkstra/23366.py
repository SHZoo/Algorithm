# boj 23366 Candy Contribution/pypy로 제출할 것
import heapq
import math

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
start, destination, candy = map(int, input().split())
distance = [0] * (n+1)

for _ in range(m):
    u, v, p = map(int, input().split())
    graph[u].append((v, 1-p*0.01))
    graph[v].append((u, 1-p*0.01))

def dijkstra(start, candy):
    hq = []
    heapq.heappush(hq, (-candy, start))
    distance[start] = candy
    while hq:
        candy, now = heapq.heappop(hq)
        if distance[now] > -candy:
            continue
        for i in graph[now]:
            cost = math.floor((-candy*i[1]))
            if distance[i[0]] < cost:
                distance[i[0]] = cost
                if i[0] == destination:
                    return
                heapq.heappush(hq, (-cost, i[0]))

dijkstra(start, candy)
print(distance[destination])
