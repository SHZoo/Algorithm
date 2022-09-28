# boj 8549 AutoStrady
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(v+1):
    parent[i] = i

edges = []
max_cost = 0

for _ in range(e):
    q, w, c = map(int, input().split())
    edges.append((c, q, w))

edges.sort()

for edge in edges:
    c, q, w = edge
    if find_parent(parent, q) != find_parent(parent, w):
        union_parent(parent, q, w)
        max_cost = max(max_cost, c)

print(max_cost)
