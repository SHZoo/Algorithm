import sys
x = int(sys.stdin.readline())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 30001

# DP 진행(Bottom-Up)
for i in range(2, x + 1) :
    d[i] = d[i-1] + 1
    if i % 2 == 0 :
        d[i] = min(d[i], d[i // 2] + 1)
    elif i % 3 == 0 :
        d[i] = min(d[i], d[i // 3] + 1)
    elif i % 5 == 0 :
        d[i] = min(d[i], d[i // 5] + 1)
        
print(d[x])