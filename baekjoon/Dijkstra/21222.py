# boj 21222 Alias
import heapq

INF = (1e10)
n, m = map(int, input().split())
distance = [INF] * (n+1)
graph = [[] for _ in range(n+1)]
dict = {}
k = 1

for _ in range(m):
    input_data = input().split()
    for i in range(2):
        if input_data[i] not in dict:
            dict[input_data[i]] = k
            k += 1
    graph[dict[input_data[0]]].append((dict[input_data[1]], int(input_data[2])))

def dijkstra(start):
    hq = []
    heapq.heappush(hq, (0, start))
    distance[start] = 0

    while hq:
        dist, now = heapq.heappop(hq)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(hq, (cost, i[0]))

t = int(input())

for _ in range(t):
    input_data = input().split()
    dijkstra(dict[input_data[0]])

    if distance[dict[input_data[1]]] == INF:
        print('Roger')
    else:
        print(distance[dict[input_data[1]]])
    
    distance = [INF] * (n+1)
