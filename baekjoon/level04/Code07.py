n = int(input())
cnt = 0
num = 0
avg = 0
student = 0
for i in range(n) :
    list_class = list(map(int, input().split()))
    cnt = 0
    num = 0
    avg = 0
    student = 0
    for j in list_class :
        if cnt == 0 :
            num = j
            cnt +=1
        else :
            avg += j
    avg = avg / num

    for j in list_class :
        if cnt == 1 :
            cnt += 1
        else :
            if j > avg :
                student += 1
    print("{:.03f}%".format((student*100)/num))