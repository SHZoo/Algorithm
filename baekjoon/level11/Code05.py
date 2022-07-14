import sys
n = sys.stdin.readline().rstrip()
array = []
for i in n :
    array.append(int(i)) 
array.sort(reverse = True)
print(*array, sep = '')