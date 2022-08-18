# boj 4722 Underground Cables/ pypy로 돌릴 것
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
while True :
    n = int(input())
    if n == 0 : break
    parent = [0] * (n+1) 
    for i in range(n+1) :
        parent[i] = i
    array = []
    edges = []
    res = 0
    for _ in range(n) :
        u, v = map(int, input().split())
        array.append((u, v))
    for i in range(len(array)-1) :
        for j in range(i+1, len(array)) :
            dist = math.sqrt((array[i][0] - array[j][0]) ** 2 + (array[i][1] - array[j][1]) ** 2)
            edges.append((dist, i+1, j+1))

    edges.sort()

    for edge in edges :
        c, q, w = edge
        if find_parent(parent, q) != find_parent(parent, w) :
            union_parent(parent, q, w)
            res += c

    print("{:.2f}".format(round(res,2)))