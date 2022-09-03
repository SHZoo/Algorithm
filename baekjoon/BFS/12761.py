# boj 12761 돌다리
from collections import deque

a, b, n, m = map(int, input().split())
visited = [False] * 100001
def bfs(start):
    queue = deque([(start, 0)])
    visited[start] = True
    while queue:
        now, cnt = queue.popleft()
        if now == m:
            return cnt
        if now < 0 or now > 100000:
            continue
        if visited[now] == True:
            continue
        visited[now] = True
        queue.append(now + 1, cnt + 1)
        queue.append(now - 1, cnt + 1)
        queue.append(now + a, cnt + 1)
        queue.append(now - a, cnt + 1)
        queue.append(now + b, cnt + 1)
        queue.append(now - b, cnt + 1)
        queue.append(now * a, cnt + 1)
        queue.append(now * b, cnt + 1)

print(bfs(n))
