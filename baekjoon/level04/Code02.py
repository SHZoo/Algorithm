cnt = 0
max = 0
list_max = []
for i in range(9) :
    a = int(input())
    if len(list_max) == 0:
        list_max.append(a)
        max = a
    else :
        if a >= max :
            list_max.append(a)
            max = a
            cnt = i
        else :
            list_max.append(a)

        
print(max)
print(cnt + 1)