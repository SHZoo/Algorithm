# boj 18352 특정 거리의 도시 찾기/ pypy로 제출할 것
import heapq

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

def bfs(start):
    hq = []
    heapq.heappush(hq, (0, start))
    res = []
    INF = (1e9)
    distance = [INF] * (n + 1)
    visited[start] = True
    while hq:
        cnt, now = heapq.heappop((hq))
        if cnt > k:
            break
        distance[now] = min(distance[now], cnt)
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                heapq.heappush(hq, (cnt+1, i))

    for i in range(1, n+1):
        if distance[i] == k:
            res.append(i)
    if res:
        return res
    else:
        return [-1]


print(*bfs(x), sep = '\n')