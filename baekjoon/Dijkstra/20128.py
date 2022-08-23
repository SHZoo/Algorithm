import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
INF = (1e15)
distance_even = [INF] * (n+1)
distance_odd = [INF] * (n+1)
distance_even_2 = [INF] * (n+1)
distance_odd_2 = [INF] * (n+1)
for _ in range(m) :
    u, v, c = map(int, input().split())
    graph[u].append((v, c))
    graph[v].append((u, c))

def dijkstra_even(start) :
    hq = []
    heapq.heappush(hq, (0, start))
    distance_even[start] = 0
    while hq :
        dist, now = heapq.heappop(hq)
        if distance_even[now] < dist and dist % 2 == 0:
            continue
        if distance_even_2[now] < dist and dist % 2 == 1 :
            continue
        for i in graph[now] :
            cost = dist + i[1]
            if cost % 2 == 0 : 
                if distance_even[i[0]] > cost :
                    distance_even[i[0]] = cost
                    heapq.heappush(hq, (cost, i[0]))
            else :
                if distance_even_2[i[0]] > cost :
                    distance_even_2[i[0]] = cost
                    heapq.heappush(hq, (cost, i[0]))


def dijkstra_odd(start) :
    hq = []
    heapq.heappush(hq, (0, start))

    while hq :
        dist, now = heapq.heappop(hq)
        if distance_odd[now] < dist and dist % 2 == 1:
            continue
        if distance_odd_2[now] < dist and dist % 2 == 0 :
            continue
        for i in graph[now] :
            cost = dist + i[1]
            if cost % 2 == 1 : 
                if distance_odd[i[0]] > cost :
                    distance_odd[i[0]] = cost
                    heapq.heappush(hq, (cost, i[0]))
            else :
                if distance_odd_2[i[0]] > cost :
                    distance_odd_2[i[0]] = cost
                    heapq.heappush(hq, (cost, i[0]))


dijkstra_even(1)
dijkstra_odd(1)

for i in range(1, n+1) :
    if distance_odd[i] == INF :
        print(-1, end = ' ')
    else :
        print(distance_odd[i], end = ' ')
    if distance_even[i] == INF :
        print(-1, end = ' ')
    else :
        print(distance_even[i], end = ' ')
    print()