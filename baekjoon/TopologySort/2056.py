# boj 2056 작업
from collections import deque
import sys
import copy

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
time_list = [0] * (n+1)

for i in range(1, n+1) :
    input_data = list(map(int, input().split()))
    time_list[i] = input_data[0]
    for j in input_data[2:] :
        graph[j].append(i)
        indegree[i] += 1

def topology_sort() :
    queue = deque()
    for i in range(1, n+1) :
        if indegree[i] == 0 :
            queue.append(i)
    time_list2 = copy.deepcopy(time_list)
    while queue :
        now = queue.popleft()
        for i in graph[now] :
            indegree[i] -= 1
            time_list2[i] = max(time_list2[i], time_list2[now] + time_list[i])
            
            if indegree[i] == 0 :
                queue.append(i)
    return max(time_list2)

print(topology_sort())