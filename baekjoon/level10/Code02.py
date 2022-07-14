import sys

test_list = [(0, 0)] 
for i in range(1, 1000000 + 1) :
    if len(str(i)) == 1 :
        num = i + i 
        test_list.append((i, num))
    elif len(str(i)) == 2 :
        num = i + int(str(i)[0]) + int(str(i)[1])
        test_list.append((i, num))
    elif len(str(i)) == 3 :
        num = i + int(str(i)[0]) + int(str(i)[1]) + int(str(i)[2])
        test_list.append((i, num))
    elif len(str(i)) == 4 :
        num = i + int(str(i)[0]) + int(str(i)[1]) + int(str(i)[2])  + int(str(i)[3])
        test_list.append((i, num))
    elif len(str(i)) == 5 :
        num = i + int(str(i)[0]) + int(str(i)[1]) + int(str(i)[2])  + int(str(i)[3]) + int(str(i)[4])
        test_list.append((i, num))
    elif len(str(i)) == 6 :
        num = i + int(str(i)[0]) + int(str(i)[1]) + int(str(i)[2])  + int(str(i)[3]) + int(str(i)[4]) + int(str(i)[5])
        test_list.append((i, num))
    else :
        test_list.append((1000000, 1000001))
n = int(sys.stdin.readline())
for i in range(1, 1000000 + 1) :
    if test_list[i][1] == n :
        print(test_list[i][0])
        break
    if i == 1000000 :
        print(0)

