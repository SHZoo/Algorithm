import sys
n, k = map(int, sys.stdin.readline().split())

list_a = list(map(int, sys.stdin.readline().split()))
list_b = list(map(int, sys.stdin.readline().split()))

for i in range(k) :
    if min(list_a) < max(list_b) :
        list_a[list_a.index(min(list_a))], list_b[list_b.index(max(list_b))] = list_b[list_b.index(max(list_b))], list_a[list_a.index(min(list_a))]
    else :
        break

print(sum(list_a))

