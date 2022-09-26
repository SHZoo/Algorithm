# boj 8347 Bug/pypy로 제출할 것
import heapq

n, m = map(int, input().split())
INF = (1e10)
graph = [[] for _ in range(n+1)]
distance = [[INF, INF] for _ in range(n+1)]

for _ in range(m):
    u, v, c = map(int, input().split())
    graph[u].append((v, c))
    graph[v].append((u, c))

def dijkstra(start):
    hq = []
    heapq.heappush(hq, (0, start))
    distance[start][0] = 0

    while hq:
        dist, now = heapq.heappop(hq)
        if dist % 2 == 0: # 거리가 짝수면
            if distance[now][0] < dist:
                continue
        elif dist % 2 == 1: # 거리가 홀수면
            if distance[now][1] < dist:
                continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost % 2 == 0:
                if distance[i[0]][0] > cost:
                    distance[i[0]][0] = cost
                    heapq.heappush(hq, (cost, i[0]))
            elif cost % 2 == 1:
                if distance[i[0]][1] > cost:
                    distance[i[0]][1] = cost
                    heapq.heappush(hq, (cost, i[0]))

dijkstra(1)

if distance[n][1] == INF:
    print(0)
else:
    print(distance[n][1])
