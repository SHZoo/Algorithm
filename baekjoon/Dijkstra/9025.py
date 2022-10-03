# boj 9025 Widest Path
import heapq

t = int(input())
INF = (1e10)

def dijkstra(start):
    hq = []
    heapq.heappush(hq, (-INF, start))
    
    while hq:
        wide, now = heapq.heappop(hq)
        if distance[now] > -wide:
            continue
        for i in graph[now]:
            new_wide = min(-wide, i[1])
            if distance[i[0]] < new_wide:
                distance[i[0]] = new_wide
                heapq.heappush(hq, (-new_wide, i[0]))

for _ in range(t):
    n, m, start, destination = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    distance = [0]*(n+1)

    for _ in range(m):
        u, v, c = map(int, input().split())
        graph[u].append((v, c))
        graph[v].append((u, c))

    dijkstra(start)
    print(distance[destination])
