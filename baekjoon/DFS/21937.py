# boj 21937 작업
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
res = 0

for _ in range(m):
    u, v = map(int, input().split())
    graph[v].append(u)

def dfs(start):
    global res

    for i in graph[start]:
        if not visited[i]:
            visited[i] = True
            res += 1
            dfs(i)


start = int(input())
dfs(start)
print(res)