# boj 14167 Moocast
import sys
input = sys.stdin.readline
n = int(input())
array = []
edges = []
for _ in range(n) :
    x, y = map(int, input().split())
    array.append((x, y))

for i in range(len(array)-1) :
    for j in range(i+1, len(array)) :
        dist = (array[i][0] - array[j][0])**2 + (array[i][1] - array[j][1])**2
        edges.append((dist, i+1, j+1))
edges.sort()    
parent = [0] * (n+1)
for i in range(n+1) :
    parent[i] = i
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

minimum_value = 0
for edge in edges :
    cost, q, w = edge
    if find_parent(parent, q) != find_parent(parent, w) :
        union_parent(parent, q, w)
        minimum_value = cost

print(minimum_value)