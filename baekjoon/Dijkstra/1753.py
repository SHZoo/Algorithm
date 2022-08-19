# boj 1753 최단경로
import heapq 
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
start = int(input())
INF = (1e9)
graph = [[] for _ in range(v+1)]
distance = [INF] * (v+1)

for _ in range(e) :
    q, w, c = map(int, input().split())
    graph[q].append((w, c)) # 방향 그래프임에 유의

def dijkstra(start) :
    hq = []
    heapq.heappush(hq, (0, start))
    distance[start] = 0

    while hq :
        dist, now = heapq.heappop(hq)
        if distance[now] < dist : # 중복 방문 방지
            continue
        for i in graph[now] :
            cost = dist + i[1]
            if distance[i[0]] > cost :
                distance[i[0]] = cost
                heapq.heappush(hq, (cost, i[0]))

dijkstra(start) 

for i in range(1, v+1) :
    if distance[i] == INF :
        print('INF')
    else :
        print(distance[i])