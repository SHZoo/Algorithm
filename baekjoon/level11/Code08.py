import sys
n = int(sys.stdin.readline())
array = []
for _ in range(n) :
    word = sys.stdin.readline().rstrip()
    array.append((word, len(word)))
array = list(set(array))

array.sort()
array = sorted(array, key = lambda array : array[1])

for i in range(len(array)) :
    print(array[i][0])