import sys
n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().strip().split()))
array_copy = array.copy()
array = list(set(array))
array.sort()
k = 0
new_array = {}

for i in array :
    new_array[i] = k
    k += 1

for i in array_copy :
    print(new_array.get(i), end = ' ')

