# boj 16167 A Great Way
from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
INF = (1e9)
distance = [INF] * (n+1)
graph = [[] for _ in range(n+1)]
dict = {i:0 for i in range(1, n+1)}

for _ in range(m) :
    a, b, c, d, e = map(int, input().split())
    if e <= 10 :
        graph[a].append((b, c))
 
    elif e > 10 :
        graph[a].append((b, c + d * (e-10)))       
visited = [False] * (n+1)
def bfs(graph, start) :
    queue = deque([(start, 0, 0)])
    array = []
    while queue :
        now, cost, num = queue.popleft()     
        for i in graph[now] :
            if i[0] == n :
                if len(array) < 1000 :
                    array.append((i[0], cost + i[1], num + 1))
                else :
                    return array
            else :
                queue.append((i[0], cost + i[1], num + 1))
    return array

res = (bfs(graph, 1))

if not res :
    print('It is not a great way.')
else :
    res = sorted(res, key = lambda res : (res[1], res[2]))
    print(res[0][1], res[0][2]+1)