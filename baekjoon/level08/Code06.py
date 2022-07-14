array = [True] * 10001 
for i in range(2, int(10001**0.5)) :
    if array[i] == True :
        for j in range(i+i, 10001, i) :
            array[j] = False

t = int(input()) 
for _ in range(t) :
    num = int(input())
    half = num // 2 
    prime_list = [i for i in range(0, num + 1) if array[i] == True]
    for i in range(half, 1, -1) :
        x = half + (half - i)
        if (i in prime_list) and (x in prime_list) :
            print(i, x)
            break
