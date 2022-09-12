# boj 25516 거리가 k이하인 트리 노드에서 사과 수확하기
from collections import deque
import sys

input = sys.stdin.readline
n, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

apple_node = list(map(int, input().split()))


def bfs():
    queue = deque([(0, 0)])
    res = 0
    while queue:
        now, cnt = queue.popleft()
        visited[now] = True
        if cnt <= k and apple_node[now] == 1:
            res += 1
        for i in graph[now]:
            if cnt + 1 <= k and not visited[i]:
                queue.append((i, cnt + 1))

    return res


print(bfs())

# 고마웠어 정말로.