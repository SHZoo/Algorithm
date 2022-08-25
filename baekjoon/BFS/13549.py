# boj 13549 숨바꼭질 3
import heapq
n, k = map(int, input().split())
visit = [False] * 100001

def bfs(start) :
    hq = []
    heapq.heappush(hq, (0, start))
    while hq :
        cnt, now = heapq.heappop(hq)
        if now == k :
            return cnt
        if now < 0 or now > 100000 :
            continue
        if visit[now] :
            continue
        visit[now] = True
        heapq.heappush(hq, (cnt+1, now+1))
        heapq.heappush(hq, (cnt+1, now-1))
        heapq.heappush(hq, (cnt, now * 2))

print(bfs(n))