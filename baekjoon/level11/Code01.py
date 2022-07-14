import sys
n = int(sys.stdin.readline())
array = []
for _ in range(n) :
    array.append(int(sys.stdin.readline()))

# 삽입 정렬
# for i in range(1, len(array)) :
#     for j in range(i, 0, -1) :
#         if array[j] < array[j-1] :
#             array[j], array[j-1] = array[j-1], array[j]

# for i in array :
#     print(i)

# 선택 정렬 
for i in range(len(array)) :
    min_index = i
    for j in range(i+1, len(array)) :
        if array[min_index] > array[j] :
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

for i in array :
    print(i)