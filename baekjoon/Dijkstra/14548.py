# boj 14548 The fastest road to banikoara
import heapq

t = int(input())
INF = (1e10)

def dijkstra(start):
    hq = []
    heapq.heappush(hq, (0, start))

    while hq:
        dist, now = heapq.heappop(hq)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(hq, (cost, i[0]))

for _ in range(t):
    n, start, destination = input().split()
    dict = {}
    dict[start] = 1
    dict[destination] = 2
    k = 3

    graph = [[] for _ in range(int(n)+1)]
    distance = [INF] * (int(n)+1)

    for _ in range(int(n)):
        input_data = input().split()

        for i in range(2):
            if input_data[i] not in dict:
                dict[input_data[i]] = k
                k += 1
        
        graph[dict[input_data[0]]].append((dict[input_data[1]], int(input_data[2])))
        graph[dict[input_data[1]]].append((dict[input_data[0]], int(input_data[2])))

    dijkstra(dict[start])
    print("{} {} {}".format(start, destination, distance[dict[destination]]))
