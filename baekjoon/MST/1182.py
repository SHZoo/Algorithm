# boj 23941 Cherries Mesh
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

t = int(input())
for p in range(1, t+1) :
    v, e = map(int, input().split())
    parent = [0] * (v+1) 
    for i in range(v+1) :
        parent[i] = i
    edges = []
    res = 0
    k = 0
    for _ in range(e) :
        x, y = map(int, input().split())
        edges.append((x, y))

    for edge in edges :
        x, y = edge
        if find_parent(parent, x) != find_parent(parent, y) :
            union_parent(parent, x, y)
            k += 1
    cost = k * 1 + ((v-1) - k) * 2
    print("Case #{}: {}".format(p, cost)) 