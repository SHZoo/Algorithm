import sys
n = int(sys.stdin.readline())
prime_number = 0


list_prime = list(map(int, sys.stdin.readline().split()))
for k in list_prime :
    if k == 1 :
        pass
    elif k == 2 :
        prime_number += 1
    else :
        for i in range(2, k) :
            if k % i == 0 :
                break
            if i == k -1 :
                prime_number += 1

print(prime_number)
