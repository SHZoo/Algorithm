import sys

set_1 = set()
set_2 = set()
n, m = map(int, sys.stdin.readline().strip().split())

for _ in range(n) :
    set_1.add(sys.stdin.readline().strip())
for _ in range(m) :
    set_2.add(sys.stdin.readline().strip())
set_3 = set_1.intersection(set_2)
list_1 = list(set_3)
list_1.sort()
print(len(list_1))
print(*list_1, sep = '\n')