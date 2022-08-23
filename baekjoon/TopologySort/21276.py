# boj 21276 계보 복원가 호석
from collections import deque

n = int(input())
people_list = input().split()
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
dict = {}
dict_2 = {}
m = int (input())
k = 1
for person in people_list :
    dict[person] = k
    dict_2[person] = []
    k += 1

for _ in range(m) :
    input_a, input_b = input().split()
    graph[dict[input_b]].append(input_a)
    indegree[dict[input_a]] += 1

def topology_sort() :
    queue = deque()
    res_list = []
    for person in people_list :
        if indegree[dict[person]] == 0 :
            queue.append(person)
            res_list.append(person)
        
    while queue :
        now = queue.popleft()
        for i in graph[dict[now]] :
            indegree[dict[i]] -= 1
            if indegree[dict[i]] == 0 :
                dict_2[now].append(i)
                queue.append(i)

    return res_list 
              


array = topology_sort()
array.sort()
print(len(array))
print(*array)
dict_2_value = dict_2.items()
dict_2_value = sorted(dict_2_value, key = lambda dict_2_value : (dict_2_value[0]))
for i in dict_2_value :
    i[1].sort()
    print(i[0], len(i[1]), *i[1])