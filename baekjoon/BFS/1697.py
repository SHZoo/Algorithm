# boj 1697 숨바꼭질
from collections import deque
n, k = map(int, input().split())
visit = [False] * 100001

def bfs(start, visit) :
    queue = deque()
    queue.append((n, 0))

    while queue :
        now, cnt = queue.popleft()
        if now < 0 or now > 100000 :
            continue
        if visit[now] == True :
            continue
        if now == k :
            return cnt
        visit[now] = True
        queue.append((now-1, cnt+1))
        queue.append((now+1, cnt+1))
        queue.append((now*2, cnt+1))

print(bfs(n, visit))