import sys

n, m = map(int, sys.stdin.readline().split())
coin_type = []
for _ in range(n) :
    coin_type.append(int(sys.stdin.readline().rstrip()))
array = [10001 for _ in range(m+1)]
array[0] = 0

for i in range(n) :
    for j in range(coin_type[i], + m + 1) :
        if array[j - coin_type[i]] != 10001 :
            array[j] = min(array[j], array[j - coin_type[i]] + 1)
    
if array[m] == 10001 :
    print(-1)
else :
    print(array[m])
