# boj 4175 Pick up sticks
import heapq

while True :
    n, m = map(int, input().split())
    if (n, m) == (0, 0) :
        break
    graph = [[] for _ in range(n+1)]
    indegree = [0] * (n+1)

    for _ in range(m) :
        u, v = map(int, input().split())
        graph[u].append(v)
        indegree[v] += 1

    def topology_sort() :
        hq = []
        for i in range(1, n+1) :
            if indegree[i] == 0 :
                heapq.heappush(hq, i)
        res_list = []

        while hq :
            now = heapq.heappop(hq)
            res_list.append(now) 
            for i in graph[now] :
                indegree[i] -= 1
                if indegree[i] == 0 :
                    heapq.heappush(hq, i)
        return res_list 

    res = topology_sort()
    if len(res) == n :
        print(*res, sep = '\n')
    else :
        print('IMPOSSIBLE')