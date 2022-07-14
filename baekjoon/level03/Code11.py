import sys

b, c = map(int, sys.stdin.readline().split())
a = []
a.extend(map(int, sys.stdin.readline().split()))
a = list(filter(lambda x : x < c , a))
for i in range(len(a)) :
    print(a[i], end = " ")