# boj 13290 Big Truck
import heapq 
import sys

input = sys.stdin.readline
INF = (1e9)

n = int(input())
time = [0]
time.extend(list(map(int, input().split())))
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
m = int(input())
result = [0] * (n+1)
for _ in range(m) :
    u, v, c = map(int, input().split())
    graph[u].append((v, c))
    graph[v].append((u, c))

def dijkstra(start) :
    hq = []
    heapq.heappush(hq, (0, start, time[start]))
    distance[start] = 0
    max_sum = 0
    while hq :
        dist, now, sum = heapq.heappop(hq)
        if distance[now] < dist :
            continue
        for i in graph[now] :
            cost = dist + i[1]
            cost_2 = sum + time[i[0]]
            if distance[i[0]] > cost :
                distance[i[0]] = cost
                if i[0] == n :
                    max_sum = cost_2
                heapq.heappush(hq, (cost, i[0], cost_2))
            elif distance[i[0]] == cost :
                if i[0] == n :
                    max_sum = max(max_sum, cost_2)
                heapq.heappush(hq, (cost, i[0], cost_2))
    return distance[n] , max_sum

u, v = dijkstra(1)
if u >= INF :
    print('impossible')
else :
    print(u, v)