import heapq 
import sys
input = sys.stdin.readline
INF = (1e9)
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
sum_time = 0
for _ in range(m) :
    u, v = map(int, input().split())
    graph[u].append((v, 1)) 
    graph[v].append((u, 1))
k, x = map(int, input().split())

def dijkstra(start) :
    hq = []
    heapq.heappush(hq, (0, start))
    distance[start] = 0

    while hq :
        dist, now = heapq.heappop(hq)
        if distance[now] < dist :
            continue
        for i in graph[now] :
            cost = dist + i[1]
            if distance[i[0]] > cost :
                distance[i[0]] = cost
                heapq.heappush(hq, (cost, i[0]))

dijkstra(1)
sum_time += distance[k] # 1번에서 k번까지 가는데 최단 시간
distance = [INF] * (n+1) 

dijkstra(k)
sum_time += distance[x] # k번에서 x번까지 가는데 최단 시간

if sum_time >= INF :
    print(-1)
else :
    print(sum_time)