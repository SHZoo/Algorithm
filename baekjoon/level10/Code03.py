import sys
n = int(sys.stdin.readline())
list_a = []
for i in range(n) :
    x, y = map(int, sys.stdin.readline().split())
    list_a.append((x, y))
rank_list = []
for i in range(len(list_a)) :
    weight = list_a[i][0] 
    height = list_a[i][1]
    rank = n
    for j in range(len(list_a)) :
        if i != j :
            if weight > list_a[j][0] and height > list_a[j][1] :
                rank -= 1
            elif (weight <= list_a[j][0] and height >= list_a[j][1]) or (weight >= list_a[j][0] and height <= list_a[j][1]) :
                rank -= 1
    rank_list.append(rank)
for i in range(len(rank_list)) :
    print(rank_list[i], end = " ")