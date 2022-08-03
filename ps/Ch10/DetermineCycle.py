# 서로소 집합을 활용한 사이클 판별 소스코드

def find_parent(parent, x) :
    if parent[x] != x :
        return find_parent(parent, parent[x])
    return x

def union_parent(parent, a, b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b :
        parent[b] = a
    else :
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1, v+1) :
    parent[i] = i

cycle = False 

for _ in range(e) :
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b) :
        cycle = True
        break
    union_parent(parent, a, b)

if cycle :
    print("cycle이 발생하였습니다.")

else :
    print("cycle이 발생하지 않았습니다.")