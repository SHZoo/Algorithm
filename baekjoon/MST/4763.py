# boj 4763 Tangled in Cables
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

cable_length = float(input())
n = int(input())
parent = [0] * (n+1)
dict = {}
for i in range(n+1):
    parent[i] = i

for i in range(1, n+1):
    input_data = input()
    dict[input_data] = i

edges = []
res = 0 

m = int(input())

for _ in range(m):
    input_data = input().split()
    edges.append((float(input_data[2]), dict[input_data[0]], dict[input_data[1]]))

edges.sort()

for edge in edges:
    c, q, w = edge
    if find_parent(parent, q) != find_parent(parent, w):
        union_parent(parent, q, w)
        res += float(c)

if res > cable_length:
    print('Not enough cable')
else:
    print('Need {:.1f} miles of cable'.format(round(res, 1)))
