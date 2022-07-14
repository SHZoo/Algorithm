import sys
dict = {0:0, 1:1, 2:1}

def fibonacci(n) :
    if n in dict :
        return dict[n]
    dict[n] = fibonacci(n-1) + fibonacci(n-2)
    return fibonacci(n-1) + fibonacci(n-2)

num = int(sys.stdin.readline())
print(fibonacci(num))