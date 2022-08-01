import heapq
import sys
input = sys.stdin.readline
INF = (1e9)
n, m, start = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
sum_city = 0 
max_city = 0
for _ in range(m) :
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

def dijkstra(start) :
    hq = []
    heapq.heappush(hq, (0, start))
    distance[start] = 0

    while hq :
        dist, now = heapq.heappop(hq)
        if distance[now] < dist :
            continue
        for i in graph[now] :
            cost=  dist + i[1]
            if distance[i[0]] > cost :
                distance[i[0]] = cost 
                heapq.heappush(hq, (cost, i[0]))

dijkstra(start) 
for i in range(1, n+1) :
    if distance[i] == INF or distance[i] == 0 :
        pass
    else :
        sum_city += 1 
        max_city = max(max_city, distance[i])

print(sum_city, max_city)