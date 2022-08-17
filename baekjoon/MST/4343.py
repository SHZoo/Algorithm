# boj 4343 Arctic Network
import math
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
for _ in range(t) :
    s, m = map(int, input().split())
    array = []
    edges = []
    for _ in range(m) :
        x, y = map(int, input().split())
        array.append((x, y))
    parent = [0] * (m+1)
    for i in range(m+1) :
        parent[i] = i
    for i in range(m-1) :
        for j in range(i+1,m) :
            dist = math.sqrt((array[i][0]-array[j][0])**2 + (array[i][1]-array[j][1])**2)
            edges.append((dist, i+1, j+1))
    edges.sort()
    res_list = []
    for edge in edges :
        cost, u, v = edge
        if find_parent(parent, u) != find_parent(parent, v) :
            union_parent(parent, u, v)
            res_list.append(cost)
    if s >= m  : 
        print(0)
    else :
        cost = "{:.2f}".format(round(res_list[(m-1)-(s-1)-1],2))
        print(cost)