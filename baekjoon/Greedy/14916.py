# boj 14916 거스름돈

n = int(input())
array = [-1]*(n+1)
array[0] = 0
for i in range(1, n+1):
    if i >= 2 and array[i-2] > -1:
        array[i] = (array[i-2]+1) if array[i] == -1 else min(array[i-2]+1, array[i])
    if i >= 5 and array[i-5] > -1:
        array[i] = (array[i-5]+1) if array[i] == -1 else min(array[i-5]+1, array[i])
print(array[n])
