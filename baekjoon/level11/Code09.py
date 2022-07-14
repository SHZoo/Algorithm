import sys
n = int(sys.stdin.readline())
array = []
i = 0
for _ in range(n) :
    x, y = sys.stdin.readline().split()
    array.append((int(x), y, i))
    i += 1

array = sorted(array, key = lambda array : (array[0], array[2]))

for i in range(len(array)) :
    print(array[i][0], array[i][1])