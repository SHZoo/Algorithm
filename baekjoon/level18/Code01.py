import sys 
n, k = map(int, sys.stdin.readline().split())
coin_type = []
for _ in range(n) :
    coin_type.append(int(sys.stdin.readline().strip()))
coin_type.sort(reverse = True)
cnt = 0

for i in coin_type :
    if i <= k :
        cnt += k//i
        k = k%i
    if k == 0 :
        break


print(cnt)