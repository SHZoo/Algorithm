# boj 6091 핑크 플로이드
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

n = int(input())
parent = [0] * (n+1)
for i in range(n+1) :
    parent[i] = i
edges = []
for i in range(n-1) :
    input_data = list(map(int, input().split()))
    for j in range(n-1-i) :
        edges.append((input_data[j], i+1, i+j+2))

edges.sort()
graph = [[]for _ in range(n+1)]

for edge in edges :
    c, q, w = edge
    if find_parent(parent, q) != find_parent(parent, w) :
        union_parent(parent, q, w)
        graph[q].append(w)
        graph[w].append(q)

for i in range(1, n+1) :
    graph[i].sort()
    print(len(graph[i]), *graph[i])