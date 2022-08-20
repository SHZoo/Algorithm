# boj 13147 Dwarves 
from collections import deque

n = int(input())
graph = [[] for _ in range(n*2+1)]
indegree = [0] * (n*2+1)
dict = {}
k = 1
for _ in range(n) :
    input_data = input().split()
    if input_data[0] not in dict :
        dict[input_data[0]] = k
        indegree[k] += 1
        k += 1
    if input_data[2] not in dict :
        dict[input_data[2]] = k
        indegree[k] += 1
        k += 1
    if input_data[1] == ">" :
        graph[dict[input_data[2]]].append(dict[input_data[0]])
        indegree[dict[input_data[0]]] += 1
    elif input_data[1] == "<" :
        graph[dict[input_data[0]]].append(dict[input_data[2]])
        indegree[dict[input_data[2]]] += 1

def topology_sort() :
    queue = deque()
    res_list = []
    for i in range(1, n*2+1) :
        if indegree[i] == 1 :
            queue.append(i)
    
    while queue :
        now = queue.popleft()
        res_list.append(now)
        for i in graph[now] :
            indegree[i] -= 1
            if indegree[i] == 1 :
                queue.append(i)
    return res_list

if len(topology_sort()) == (k-1) :
    print('possible')
else :
    print('impossible')