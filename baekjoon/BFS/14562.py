# boj 14562 태권왕
from collections import deque

c = int(input())


def bfs(start, destination):
    queue = deque([(start, 0, destination)])

    while queue:
        now, cnt, des = queue.popleft()
        if now == des:
            return cnt
        if now + now <= des + 3:
            queue.append((now + now, cnt + 1, des + 3))
        if now + 1 <= des:
            queue.append((now + 1, cnt + 1, des))


for _ in range(c):
    s, t = map(int, input().split())
    visited = [False] * 101
    print(bfs(s, t))