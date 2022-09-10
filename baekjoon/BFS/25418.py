# boj 25418 정수 a를 k로 만들기
import heapq

a, k = map(int, input().split())
visited = [False] * (k+1)

def bfs():
    hq = []
    heapq.heappush(hq, (0, a))

    while hq:
        cnt, now = heapq.heappop(hq)
        if now == k:
            return cnt
        if now+1 <= k and not visited[now+1]:
            heapq.heappush(hq, (cnt+1, now+1))
        if now*2 <= k and not visited[now*2]:
            heapq.heappush(hq, (cnt+1, now*2))
        if now+1 <= k:
            visited[now+1] = True
        if now*2 <= k:
            visited[now*2] = True

print(bfs())