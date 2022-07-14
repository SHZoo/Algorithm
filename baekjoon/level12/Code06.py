import sys
s1 = set()
s2 = set()
n, m = map(int, sys.stdin.readline().strip().split())

s1.update(list(map(int, sys.stdin.readline().strip().split())))
s2.update(list(map(int, sys.stdin.readline().strip().split())))

s1.symmetric_difference_update(s2)
print(len(s1))
