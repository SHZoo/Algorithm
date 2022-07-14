import sys
import math

m, n = map(int, sys.stdin.readline().split())

# 1 2 .1 3. 2 2 . 2 3 .3 3  
prime_list = []

for i in range(2, math.ceil(math.sqrt(n+1))) :
    if i == 2 :
        prime_list.append(i)
    else :
        for j in range(2, i) :
            if i % j == 0 :
                break
            if j == i - 1 :
                prime_list.append(i)
if (m, n) == (1, 2) or (m, n) == (2, 2) :
    print(2)
elif (m, n) == (1, 3) or (m, n) == (2, 3) :
    print(2, 3, sep = "\n")
elif (m, n) == (3, 3)  :
    print(3)
for i in range(m, n + 1) :
    if i in prime_list and i != 1:
        print(i)
    elif not(i in prime_list) and i != 1 :
        for j in range(len(prime_list)) :
            if i % prime_list[j] == 0 :
                break
            if j == len(prime_list) - 1 :
                print(i)
                
