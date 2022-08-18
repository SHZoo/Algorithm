# boj 16405 Treehouses
import sys
import math
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

n, e, p = map(int, input().split())
parent = [0] * (n+1)
for i in range(1, n+1) :
    parent[i] = i
array = []
edges = []
for _ in range(n) :
    x, y = map(float, input().split())
    array.append((x, y))

for _ in range(p) :
    x, y = map(int, input().split())
    union_parent(parent, x, y)

res = 0
for i in range(n-1) :
    for j in range(i+1, n) :
        if i <= e-1 and j <= e-1 :
            edges.append((0, i+1, j+1))
        else :
            dist = math.sqrt((array[i][0]-array[j][0])**2 +(array[i][1] - array[j][1])**2)
            edges.append((dist, i+1, j+1))
edges.sort()

for edge in edges :
    c, q, v = edge
    if find_parent(parent, q) != find_parent(parent, v) :
        union_parent(parent, q, v)
        res += c

print("{:.3f}".format(round(res,3)))