# boj 6589 Heavy Cargo
import heapq

def dijkstra(start):
    hq = []
    heapq.heappush(hq, (-1e10, start))
    distance[start] = 0

    while hq:
        max_load, now = heapq.heappop(hq)
        if distance[now] > -max_load:
            continue
        for i in graph[now]:
            if distance[i[0]] < min(i[1], -max_load):
                distance[i[0]] = min(i[1], -max_load)
                heapq.heappush(hq, (-min(i[1], -max_load), i[0]))
t = 0
while True:
    t += 1
    n, m = map(int, input().split())
    if (n, m) == (0, 0): break

    graph = [[] for _ in range(n+1)]
    distance = [0] * (n+1)
    dict = {}
    k = 1

    for _ in range(m):
        input_data = input().split()
        for i in range(2):
            if input_data[i] not in dict:
                dict[input_data[i]] = k
                k += 1
        graph[dict[input_data[0]]].append((dict[input_data[1]], int(input_data[2])))
        graph[dict[input_data[1]]].append((dict[input_data[0]], int(input_data[2])))

    start, destination = input().split()
    dijkstra(dict[start])
    print("Scenario #{}".format(t))
    print("{} tons".format(distance[dict[destination]]))
    print()
