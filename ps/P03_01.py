# 내 코드
n, m, k = map(int, input().split())

list_sort = list(map(int, input().split()))
list_sort.sort()

result = 0
count = 0
limit = 0

while m > count :
    if limit < k :
        result += list_sort[-1]
        count += 1
        limit += 1
    else :    
        result += list_sort[-2]
        count += 1
        limit = 0

# print(result)

# 책 코드
# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))

# data.sort() # sort는 파괴함수
# first = data[-1]
# second = data[-2]
# result = 0

# while True :
#     for i in range(k):
#         if m == 0 :
#             break
#         result += first
#         m -= 1
#     if m == 0 :
#         break
#     result += second
#     m -= 1
# print(result)