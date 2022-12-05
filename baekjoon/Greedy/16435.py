# boj 16435 스네이크버드

n, m = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

for i in array:
    if m >= i:
        m += 1
    else:
        break

print(m)
