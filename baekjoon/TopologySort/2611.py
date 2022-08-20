# boj 2611 자동차경주
from collections import deque

n = int(input())
m = int(input())

graph =[[] for _ in range(n+1)]
indegree = [0] * (n+1)
time = [0] * (n+1)
dict = {i:0 for i in range(1, n+1)}
for _ in range(m) :
    u, v, r = map(int, input().split())
    graph[u].append((v, r))
    indegree[v] += 1

def topology_sort() :
    queue = deque([1])
    res_list = []
    k = 0
    for i in range(2, n+1) :
        if indegree[i] == 0 :
            queue.append(i)

    while queue :
        now = queue.popleft()
        if k == 1 and now == 1 :  # 1에서 출발한 것이 도착 후 재출발 금지
            continue
        if now == 1 :
            k += 1
        res_list.append(now)
        for i in graph[now] :
            indegree[i[0]] -= 1
            if time[i[0]] < time[now] + i[1] :
                dict[i[0]] = now
            time[i[0]] = max(time[i[0]], time[now] + i[1])
            if indegree[i[0]] == 0 :
                queue.append(i[0])
    return time[1]


print(topology_sort())
route_list = [1]
i = 1
while True :
    if dict[i] == 1 :
        route_list.append(1)
        break
    else :
        route_list.append(dict[i])
        i = dict[i]

route_list = list(reversed(route_list))
for i in route_list :
    print(i, end = ' ')