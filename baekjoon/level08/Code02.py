import sys
m = int(sys.stdin.readline())
n = int(sys.stdin.readline())

list_prime = []
for i in range(m, n+ 1) :
    if i == 1 :
        pass
    elif i == 2 :
        list_prime.append(i)
    else :
        for k in range(2, i) :
            if i % k == 0 :
                break
            if k == i - 1 :
                list_prime.append(i)

if len(list_prime) == 0 :
    print(-1)
else :
    print(sum(list_prime))
    print(min(list_prime))
    
