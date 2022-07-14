import sys
n = int(sys.stdin.readline())
array_mode = [0] * 8001 
array = []
for _ in range(n) :
    num = int(sys.stdin.readline())
    array.append(num)
    array_mode[num+4000] += 1

if float("{:.1f}".format(sum(array)/n)) < 0 :
    avg = int(float("{:.1f}".format(sum(array)/n)) - 0.5)
else :
    avg = int(float("{:.1f}".format(sum(array)/n)) + 0.5)

array.sort()
median = array[int(n/2)]

if array_mode.count(max(array_mode)) >= 2 :
    array_mode[array_mode.index(max(array_mode))] = 0
    mode_mode = array_mode.index(max(array_mode)) - 4000
else :
    mode_mode = array_mode.index(max(array_mode)) - 4000

range = max(array) - min(array)

print(avg, median, mode_mode, range, sep = '\n')