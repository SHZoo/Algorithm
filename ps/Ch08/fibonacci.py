dict = {1:1, 2:1}

def fibonacci(n) : 
    if n in dict :
        return dict[n]
    dict[n] = fibonacci(n-1) + fibonacci(n-2)
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(500))
