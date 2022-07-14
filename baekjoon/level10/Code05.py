import sys
end_list = []
for i in range(666, 10000000 + 1) :
    cnt = 0
    for j in range(0,len(str(i))) :
        if str(i)[j] == '6' :
            cnt += 1
            if cnt == 3 :
                end_list.append(i)
        else :
            cnt = 0
    if len(end_list) == 10000 :
        break

num = int(sys.stdin.readline())

print(end_list[num - 1])