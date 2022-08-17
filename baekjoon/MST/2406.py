# boj 2406 안정적인 네트워크
import sys
input = sys.stdin.readline

def find_parent(parent, x) :
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b :
        parent[b] = a
    else :
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v+1)
for i in range(v+1) :
    parent[i] = i

for _ in range(e) :
    x, y = map(int, input().split())
    union_parent(parent, x, y)

graph = []
edges = []

for _ in range(v) :
    graph.append(list(map(int, input().strip().split())))

for i in range(1, v-1) :
    for j in range(i+1, v) :
        edges.append((graph[i][j], i+1, j+1))
edges.sort()
k = 0
res = 0
res_list = []

while k < (v-1) - e - 1 :
    for edge in edges :
        c, q, w = edge
        if find_parent(parent, q) != find_parent(parent, w) :
            union_parent(parent, q, w)
            res += c
            k += 1
            res_list.append((q, w))

print(res, k)
for i in res_list :
    x, y = i
    print(x, y)