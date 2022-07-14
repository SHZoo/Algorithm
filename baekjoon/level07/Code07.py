import sys
import math
n = int(sys.stdin.readline())
k = math.ceil(n/5)

if k * 5 == n :
    print(k)
else :
    for i in range(k-1, -1, -1) :
        rest = n - (i * 5)
        case_5 = i
        if rest % 3 == 0 :
            case_3 = rest // 3
            print(case_5 + case_3)
            break
        else :
            pass
        if i == 0 :
            print(-1)

