count = 0
a = b = input()
while (int(a) == int(b) and count == 0) or (int(a) != int(b) and count != 0) :
    if int(a) >= 0 and int(a) <= 9 :
        if len(a) == 1 :
            a = a + a
            count += 1
        else :
            a = a[-1] + a[-1] 
            count += 1
    elif int(a) >= 10 and int(a) <= 99 :
        if (int(a[0]) + int(a[1])) >= 10 :
            a = a[1] + str(int(a[0]) + int(a[1]))[1]
            count += 1
        else :
            a = a[1] + str(int(a[0]) + int(a[1]))
            count += 1

print(count)
