array = [True] * 10001
def d(n) :
    if len(str(n)) == 1 :
        n = n + n
        array[n] = False
    elif len(str(n)) == 2 :
        n = n + int(str(n)[0]) + int(str(n)[1])
        array[n] = False
    elif len(str(n)) == 3 :
        n = n + int(str(n)[0])  + int(str(n)[1]) + int(str(n)[2])
        array[n] = False
    elif len(str(n)) == 4 :
        n = n + int(str(n)[0])  + int(str(n)[1]) + int(str(n)[2]) + int(str(n)[3])
        if n <= 10000:
            array[n] = False
    
    
for i in range(1, 10000) :
    d(i)
self_list = [i for i in range(1, 10000 + 1) if array[i] == True]
for i in self_list :
    print(i)
    
        