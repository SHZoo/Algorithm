# boj 14248 점프 점프
from collections import deque
import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().strip().split()))
visited = [False] * (n + 1)
start = int(input())


def bfs(start):
    queue = deque([start])
    res = 0
    while queue:
        now = queue.popleft()
        visited[now] = True
        new_now = now + arr[now - 1]
        if new_now <= n and not visited[new_now]:
            queue.append(new_now)
        new_now = now - arr[now - 1]
        if new_now > 0 and not visited[new_now]:
            queue.append(new_now)

    for i in range(1, n + 1):
        if visited[i] == True:
            res += 1

    return res


print(bfs(start))