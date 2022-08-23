# boj 17940 지하철
import heapq

n, destination = map(int, input().split())
subway_list = []

for _ in range(n) :
    subway_list.append(int(input()))

graph = [[] for _ in range(n)]
INF = (1e9)
distance = [INF] * n
transfer = [INF] * n

for i in range(n) :
    input_data = list(map(int, input().split()))
    for j in range(i+1, n) :
        if input_data[j] == 0 :
            continue
        graph[i].append((j, input_data[j]))
        graph[j].append((i, input_data[j]))

def dijkstra(start) :
    hq = []
    heapq.heappush(hq, (0, start, 0))
    distance[start] = 0
    transfer[start] = 0
    while hq :
        trans, now, dist = heapq.heappop(hq)
        if transfer[now] < trans :
            continue
        for i in graph[now] :
            cost = dist + i[1]
            if subway_list[now] != subway_list[i[0]] :
                if transfer[i[0]] >= trans + 1 :
                    if distance[i[0]] > cost :
                        distance[i[0]] = cost
                        transfer[i[0]] = trans+1
                        heapq.heappush(hq, (trans+1, i[0], cost))
            elif subway_list[now] == subway_list[i[0]] :
                if transfer[i[0]] >= trans :
                    if distance[i[0]] > cost :
                        transfer[i[0]] = min(transfer[i[0]], trans)
                        distance[i[0]] = cost
                        heapq.heappush(hq, (trans, i[0], cost))


dijkstra(0)
print(transfer[destination], distance[destination])