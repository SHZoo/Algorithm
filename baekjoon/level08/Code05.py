import math
import sys

array = [0] *246913
array[2] = 1
prime_list = [2]

for i in range(3, math.ceil(math.sqrt(123456*2))) :
    for j in range(2, i) :
        if i % j == 0 :
            break
        if j == i - 1 :
            prime_list.append(i)
            array[i] = 1
for i in range(3, 246913) :
    for j in range(len(prime_list)) :
        if i % prime_list[j] == 0 :
            break
        if j == len(prime_list) - 1 :
            array[i] = 1

while True :
    num = int(sys.stdin.readline())
    cnt = 0
    if num == 0 :
        break
    for i in range(num + 1 ,num * 2 +1) :
        if array[i] == 1 :
            cnt += 1
        else :
            pass

    print(cnt)
    



