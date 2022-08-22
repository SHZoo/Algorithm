# boj 17242 KaKa & Bebe
import heapq 

n, m = map(int, input().split())
INF = (1e20)
graph = [[] for _ in range(n)]
distance = [INF] * n

for _ in range(m) :
    u, v, c1, c2 = map(int, input().split())
    if c1 > 1000 or c2 > 1000 :
        continue
    graph[u].append((v, c1, c2))
    graph[v].append((u, c1, c2))

def dijkstra(start) :
    hq = []
    heapq.heappush(hq, (0, 0, start))
    distance[start] = 0
    dict = {i : [] for i in range(n)}
    while hq :
        kaka, bebe , now = heapq.heappop(hq)
        if (kaka, bebe) in dict[now] :
            continue
        dict[now].append((kaka, bebe))
        for i in graph[now] :
            cost_1 = kaka + i[1]
            cost_2 = bebe + i[2]
            new_stress = cost_1 * cost_2
            if cost_1 > 1000 or cost_2 > 1000 :
                continue
            if distance[i[0]] >= new_stress :
                distance[i[0]] = new_stress 
                heapq.heappush(hq, (cost_1, cost_2, i[0]))

dijkstra(0)
if distance[n-1] == INF :
    print(-1)
else :
    print(distance[n-1])