# boj 25430 다이제스타
import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
INF = 1e20
distance = [INF] * (n+1)
before = [INF] * (n+1)
for _ in range(m) :
    u, v, c = map(int, input().split())
    graph[u].append((v, c))
    graph[v].append((u, c))

start, destination = map(int, input().split())

def dijkstra(start) :
    hq = []
    heapq.heappush(hq, (0, start, 0))
    distance[start] = 0
    while hq :
        dist, now, bef = heapq.heappop(hq)
        if before[now] < bef :
            continue
        before[now] = bef
        
        for i in graph[now] :
            if bef >= i[1] :
                continue
            cost = dist + i[1]
            distance[i[0]] = min(distance[i[0]], cost)
            heapq.heappush(hq, (cost, i[0], i[1]))


dijkstra(start)
if distance[destination] == INF :
    print('DIGESTA')
else :
    print(distance[destination])