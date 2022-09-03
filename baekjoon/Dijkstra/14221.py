# boj 14221 편의점
import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
INF = (1e10)
distance = [INF] * (n+1)
hq = []
for _ in range(m):
    u, v, c = map(int, input().split())
    graph[u].append((v, c))
    graph[v].append((u, c))

def dijkstra():
    while hq:
        dist, now = heapq.heappop(hq)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(hq, (cost, i[0]))

a, b = map(int, input().split())
home_list = list(map(int, input().split()))
conve_list = list(map(int, input().split()))
home_list.sort()

for i in conve_list:
    heapq.heappush(hq, (0, i))

dijkstra()
min_dist = INF
mid_node = 0

for i in home_list:
    if distance[i] < min_dist:
        min_dist = distance[i]
        min_node = i

print(min_node)