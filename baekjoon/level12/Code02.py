import sys 
n, m = map(int, sys.stdin.readline().split())
s = set()
k = list()
cnt = 0

for _ in range(n) :
    s.add(sys.stdin.readline().strip())

for _ in range(m) :
    k.append(sys.stdin.readline().strip())

for i in k :
    if i in s :
        cnt += 1

print(cnt)

