# boj 2252 줄 세우기
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for _ in range(m) :
    u, v = map(int, input().split())
    graph[u].append(v)
    indegree[v] += 1

def topology_sort() :
    queue = deque()
    for i in range(1, n+1) :
        if indegree[i] == 0 :
            queue.append(i)
    res_list = []
    while queue :
        now = queue.popleft()
        res_list.append(now)
        for i in graph[now] :
            indegree[i] -= 1
            if indegree[i] == 0 :
                queue.append((i))

    return res_list

print(*topology_sort())