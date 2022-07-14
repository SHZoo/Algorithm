import sys

n = int(sys.stdin.readline())
list_1 = list(map(int, sys.stdin.readline().strip().split()))
m = int(sys.stdin.readline())
list_2 = list(map(int, sys.stdin.readline().strip().split()))

dict = {}

for i in list_1 :
    if i not in dict :
        dict[i] = 1
    else :
        dict[i] = dict[i] + 1

for i in list_2 :
    if i in dict :
        print(dict[i], end = ' ')
    else :
        print(0, end = ' ')