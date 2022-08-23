# boj 13911 집 구하기
import heapq
import sys

input = sys.stdin.readline
INF = (1e12)
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance_macdonald = [INF] * (n+1)
distance_starbucks = [INF] * (n+1)
hq_1 = []
hq_2 = []
for _ in range(m) :
    u, v, c = map(int, input().split())
    graph[u].append((v, c))
    graph[v].append((u, c))

def dijkstra(hq, distance) :
    while hq :
        dist, now = heapq.heappop(hq) 
        if distance[now] < dist :
            continue
        for i in graph[now] :
            cost = dist + i[1]
            if distance[i[0]] > cost :
                distance[i[0]] = cost 
                heapq.heappush(hq, (cost, i[0]))


mac, x = map(int, input().split())
mac_list = list(map(int, input().split()))
for i in mac_list :
    hq_1.append((0, i))

star, y = map(int, input().split())
star_list = list(map(int, input().split()))
for i in star_list :
    hq_2.append((0, i))

dijkstra(hq_1, distance_macdonald)
dijkstra(hq_2, distance_starbucks)
res = INF

nomination = set(range(1, n+1)).difference(set(mac_list).union(set(star_list)))

for i in nomination :
    if distance_macdonald[i] <= x and distance_starbucks[i] <= y :
        res = min(res, distance_macdonald[i] + distance_starbucks[i])

if res == INF :
    print(-1)
else :
    print(res)