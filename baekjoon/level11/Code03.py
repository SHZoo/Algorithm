import sys

n = int(sys.stdin.readline())
array = [0] * 10001
for _ in range(n) :
    num = int(sys.stdin.readline())
    array[num] += 1

for i in range(len(array)) :
    for _ in range(array[i]) :
        print(i)