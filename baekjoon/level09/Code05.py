import sys 
n = int(sys.stdin.readline())

def hanoi(n, start, aux, end) :

    if n == 1 :
        print(start, end)
        return
    hanoi(n-1, start, end, aux)
    print(start, end)
    hanoi(n-1, aux, start, end)

print(2**n - 1)
hanoi(n, 1, 2, 3)
