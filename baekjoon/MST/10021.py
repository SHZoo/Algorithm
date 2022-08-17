# boj 10021 Watering the Fields
import heapq

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

e, c = map(int, input().split())
parent = [0] * e
for i in range(e) :
    parent[i] = i

array = []
for _ in range(e) :
    x, y = map(int, input().split())
    array.append((x, y))

edges = []
for i in range(e-1) :
    for j in range(i+1, e) :
        dist = (array[i][0] - array[j][0]) **2 + (array[i][1] - array[j][1]) **2
        if dist < c :
            continue
        heapq.heappush(edges, (dist, i, j))

res = 0
k = 0
while edges :
    cost, u, v = heapq.heappop(edges)
    if find_parent(parent, u) != find_parent(parent, v) :
        union_parent(parent, u, v)
        res += cost 
        k += 1
    if k == e-1 :
        break

if k == e-1 :
    print(res)
else :
    print(-1)