# boj 24846 Army of Clones/pypy로 제출할 것
import heapq
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [0] * (n+1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

clone = int(input())
enemy = list(map(int, input().split()))

def dijkstra(start):
    hq = []
    if enemy[0] < clone:
        distance[start] = clone
        heapq.heappush(hq, (-clone, start))
    else:
        distance[start] = clone//2
        heapq.heappush(hq, (-(clone//2), start))

    while hq:
        cln, now = heapq.heappop(hq)
        cln = -cln
        if distance[now] > -cln:
            continue
        for i in graph[now]:
            if cln > enemy[i-1] and distance[i] < cln:
                heapq.heappush(hq, (-cln ,i))
                distance[i] = cln
            elif cln <= enemy[i-1] and distance[i] < cln//2 :
                heapq.heappush(hq, (-(cln//2), i))
                distance[i] = cln//2
dijkstra(1)
print(distance[n])
