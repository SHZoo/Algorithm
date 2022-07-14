import sys
n = int(sys.stdin.readline())
set_1 = set(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
list_1 = list(map(int, sys.stdin.readline().split()))
set_2 = set(list_1)

set_intersection = set_2.intersection(set_1)
for i in list_1 :
    if i in set_intersection :
        print(1, end = ' ')
    else :
        print(0, end = ' ')