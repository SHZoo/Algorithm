import sys
n = int(sys.stdin.readline())
array = []
for _ in range(n) :
    x, y = map(int, sys.stdin.readline().split())
    array.append((x, y))

array = sorted(array, key = lambda array : (array[1], array[0]))

sum = 0
last_time = 0
for i in range(len(array)) :
    if i == 0 :
        last_time = array[i][1]
        sum += 1
    else :
        if array[i][0] >= last_time :
            last_time = array[i][1]
            sum += 1
        else :
            pass
print(sum)
