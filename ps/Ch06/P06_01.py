# 내 코드
import sys
array = []
n = int(sys.stdin.readline())
for _ in range(n) :
    array.append(int(sys.stdin.readline()))
array.sort()
array = list(reversed(array))

for i in array :
    print(i, end = " ") 

# 책 코드
# n = int(input())

# array = []
# for i in range(n) :
#     array.append(int(input()))

# array = sorted(array, reverse = True )

# for i in array :
#     print(i, end = ' ')