# boj 16302 Jurassic jigsaw
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
parent = [0] * (v)
for i in range(v) :
    parent[i] = i

array = []
edges = []
res_list = []
res = 0 
for _ in range(v) :
    array.append(input().strip())

for i in range(len(array)-1) :
    for j in range(i+1, len(array)) :
        dist = 0
        for k in range(e) :
            if array[i][k] != array[j][k] :
                dist += 1
        edges.append((dist, i, j))

edges.sort()

for edge in edges :
    c, q, w = edge
    if find_parent(parent, q) != find_parent(parent, w) :
        union_parent(parent, q, w)
        res += c
        res_list.append((q, w))

print(res)
for i in res_list :
    u, v = i
    print(u, v)