# boj 1005 ACM Craft / pypy로 제출할 것
from collections import deque
import sys
import copy 
imput = sys.stdin.readline

t = int(input())

for _ in range(t) :
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    indegree = [0] * (n+1)
    time = [0]
    time.extend(list(map(int, input().split())))
    
    for _ in range(m) :
        u, v = map(int, input().split())
        graph[u].append(v)
        indegree[v] += 1
    destination = int(input())
    def topology_sort() :
        queue = deque()
        result = copy.deepcopy(time)
        for i in range(1, n+1) :
            if indegree[i] == 0 :
                queue.append(i)
        
        while queue :
            now = queue.popleft()
            for i in graph[now] :
                indegree[i] -= 1
                result[i] = max(result[i], result[now] + time[i])
                if indegree[i] == 0 :
                    queue.append(i)
    
        return result[destination]
    
    print(topology_sort())