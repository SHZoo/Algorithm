import re


n = int(input())
array = []

def setting(data) :
    return data[1]

for _ in range(n) :
    x, y = input().split()
    array.append((x, y))

result = sorted(array, key = setting)
for i in range(n) :
    print(result[i][0], end = " ")
