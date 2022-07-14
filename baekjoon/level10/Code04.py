import sys
m, n = map(int, sys.stdin.readline().split())
array = []
array_list = []
game_list = []
for _ in range(m) :
    array.append(sys.stdin.readline().rstrip())

for i in range(0, m - 7) :
    new_array = array[0+i:8+i]
    array_list.append(new_array)

for i in array_list :
    for k in range(0, n-7) :
        test_list = []
        for j in i :
            test_list.append(j[0+k:8+k])
        game_list.append(test_list)
comparison_list = []
for game in game_list :
    num = 0
    cnt = 0
    count = 0
    for g in game :
        if num % 2 == 0 :
            for i in range(0,8,2) :
                if g[i] != 'W' :
                    cnt += 1
                else :
                    count += 1
            for j in range(1,8,2) :
                if g[j] != 'B' :
                    cnt += 1
                else :
                    count += 1
            num += 1
        else :
            for i in range(0,8,2) :
                if g[i] != 'B' :
                    cnt += 1
                else :
                    count += 1
            for j in range(1,8,2) :
                if g[j] != 'W' :
                    cnt += 1
                else :
                    count += 1
            num += 1
    comparison_list.append(min(cnt, count)) 

print(min(comparison_list))