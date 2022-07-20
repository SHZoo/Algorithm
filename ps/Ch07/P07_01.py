import sys
n = int(sys.stdin.readline())
array_1 = list(map(int, sys.stdin.readline().strip().split()))
m = int(sys.stdin.readline())
array_2 = list((map(int, sys.stdin.readline().strip().split())))
array_1.sort()
def binary_search(array, target, start, end) :
    if start > end :
        return None
    mid = (start + end) // 2
    if target == array[mid] :
        return mid 
    elif array[mid] < target :
        return binary_search(array, target, mid + 1, end)
    elif array[mid] > target :
        return binary_search(array, target, start, mid - 1)


for i in array_2 :
    if binary_search(array_1, i, 0, n-1) == None :
        print('no', end = ' ')
    else :
        print('yes', end = ' ')