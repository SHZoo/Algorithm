# boj 13151 Model Railroad
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

v, e, l = map(int, input().split())
edges = []
res = 0
sum = 0
parent = [0] * (v+1)
for i in range(v+1) :
    parent[i] = i
for _ in range(l) :
    q, w, c = map(int, input().split())
    edges.append((c, q, w))
    sum += c
for _ in range(e-l) :
    q, w, c = map(int, input().split())
    edges.append((c, q, w))

edges.sort()
k = 0
for edge in edges :
    c, q, w = edge
    if find_parent(parent, q) != find_parent(parent, w) :
        union_parent(parent, q, w)
        res += c
        k += 1

if k == v-1 :
    if res <= sum :
        print("possible")
    else :
        print("impossible")
else :
    print("impossible")