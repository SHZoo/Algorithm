# boj 3803 Networking
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

while True:
    try:
        v, e = map(int, input().split())
        parent = [0] * (v+1)

        for i in range(1, v+1):
            parent[i] = i
        edge_list = []
        res = 0

        for _ in range(e):
            q, w, c = map(int, input().split())
            edge_list.append((c, q, w))
        edge_list.sort()

        for edge in edge_list:
            c, q, w = edge
            if find_parent(parent, q) != find_parent(parent, w):
                union_parent(parent, q, w)
                res += c

        print(res)
        input()
    except:
        break