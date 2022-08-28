# boj 13913 숨바꼭질4
from collections import deque

n, k = map(int, input().split())
path = []
visited = [-1] * 100001

def bfs(start, target):
    queue = deque()
    queue.append((start, 0))
    visited[start] = start

    while queue:
        now, cnt = queue.popleft()
        if now == target:
            idx = now
            while idx != start:
                path.append(idx)
                idx = visited[idx]
            path.append(start)
            return cnt
        if now+1 <= 100000 and visited[now+1] == -1:
            queue.append((now+1, cnt+1))
            visited[now+1] = now
        if now-1 >= 0 and visited[now-1] == -1:
            queue.append((now-1, cnt+1))
            visited[now-1] = now
        if now*2 <= 100000 and visited[now*2] == -1:
            queue.append((now*2, cnt+1))
            visited[now*2] = now

print(bfs(n, k))
print(*path[::-1])