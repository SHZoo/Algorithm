# 11085 군사 이동/ Union-Find
import sys
import heapq
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
start, destination = map(int, input().split())
parent = [0] * (v)
for i in range(v) :
    parent[i] = i

edges = []
for _ in range(e) :
    q, w, c = map(int, input().split())
    edges.append((c, q, w))

edges.sort(reverse =  True)
res_list = []
for edge in edges :
    c, q, w = edge
    if find_parent(parent, q) != find_parent(parent, w) :
        union_parent(parent, q, w)
        heapq.heappush(res_list, c)
    if find_parent(parent, start) == find_parent(parent, destination) :
        break
print(heapq.heappop(res_list))