n = int(input())
start_after = 1
start_before = 0

acc = 5
while n > start_after :
    start_before = start_after + 1
    start_after += acc
    acc += 4
if n == 1 :
    print("{}/{}".format(1, 1))

elif n <= (start_after + start_before)//2 :
    a = n - start_before + 1
    if n < (start_after + start_before)//2 :
        b = (start_after - start_before)//2 + 1 - a
    else :
        b = (start_after - start_before)//2 + 2 - a
    
    print("{}/{}".format(a, b))
elif n > (start_after + start_before)//2 :
    b = n - (start_after + start_before)//2 + 1
    a = (start_after - start_before)//2 + 2 - b
    print("{}/{}".format(a, b))