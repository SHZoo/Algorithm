# boj 10661 Median Tree 
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

while True :
    n, m = map(int, input().split())
    if (n, m) == (0, 0) :
        break
    edges = []
    k = 0
    parent = [0] * (n+1)

    for i in range(1, n+1) :
        parent[i] = i

    for _ in range(m) :
        u, v, c = map(int, input().split())
        edges.append((c, u, v))
    edges.sort()
    
    for edge in edges :
        c, u, v = edge
        if find_parent(parent, u) != find_parent(parent, v) :
            union_parent(parent, u, v)
            k += 1
        if n == 2 and k == 1 :
            print(c)
            break
        elif n > 2 :
            if k == n // 2 :
                print(c)
                break