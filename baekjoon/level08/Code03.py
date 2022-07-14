import sys
n = int(sys.stdin.readline())

if n == 1 :
    pass
elif n == 2 :
    print(2)

else :
    for i in range(2, n+1) :
        while n % i == 0 :
            n //= i 
            print(i)
