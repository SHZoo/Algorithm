# boj 16227 의약품 수송
import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n+2)]
INF = (1e9)
distance = [INF] * (n+2)

for _ in range(m) :
    u, v, c = map(int, input().split())
    if c > 100 :
        continue
    graph[u].append((v, c))
    graph[v].append((u, c))

def dijkstra(start) :
    hq = []
    heapq.heappush(hq, (0, start, 0))
    distance[start] = 0

    while hq :
        dist, now, dust = heapq.heappop(hq)
        if distance[now] < dist :
            continue
        for i in graph[now] :
            cost = dist + i[1]
            if cost <= 100 :
                if i[0] == n+1 :
                    distance[i[0]] = min(distance[i[0]], cost + dust)
                else :
                    if distance[i[0]] > cost + dust:
                        distance[i[0]] = cost + dust
                        heapq.heappush(hq, (cost, i[0], dust))
            elif cost > 100  :
                if distance[i[0]] > cost + dust + 5 :
                    distance[i[0]] = cost + dust + 5
                    heapq.heappush(hq, (i[1], i[0], dust + dist + 5))

dijkstra(0)
print(distance[n+1])

                


