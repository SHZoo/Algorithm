# boj 5014 스타트링크
import heapq

f, s, g, u, d = map(int, input().split())
visited = [False] * (1000001)

def bfs(start):
    hq = []
    heapq.heappush(hq, (0, start))

    while hq:
        cnt, now = heapq.heappop(hq)
        if now == g:
            return cnt
        if now <= 0 or now > f:
            continue
        if visited[now]:
            continue
        visited[now] = True
        heapq.heappush(hq, (cnt+1, now + u))
        heapq.heappush(hq, (cnt+1, now - d))

    return None

res = bfs(s)

if res == None:
    print("use the stairs")
else :
    print(res)