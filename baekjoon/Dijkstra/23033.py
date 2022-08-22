# boj 23033 집에 빨리 가고 싶어!
import heapq 
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
INF = (1e9)
distance = [INF] * (n+1)


for _ in range(m) :
    u, v, c, w = map(int, input().split())
    graph[u].append((v, c, w))


def dijkstra(start) :
    hq = []
    heapq.heappush(hq, (0, start))
    distance[start] = 0

    while hq :
        dist, now = heapq.heappop(hq)
        if distance[now] < dist :
            continue
        for i in graph[now] :
            if dist % i[2] == 0 :
                cost = dist + i[1]
            else :
                cost = (dist // i[2] + 1) *i[2] + i[1]
            if distance[i[0]] > cost :
                distance[i[0]] = cost 
                heapq.heappush(hq, (cost, i[0]))

dijkstra(1)
print(distance[n])