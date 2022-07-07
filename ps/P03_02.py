# 내 코드
n, m = map(int, input().split())
list_card = []
result = 0

for i in range(n):
    list_card.append(list(map(int, input().split())))

for card in list_card :
    result = max(result, min(card))

print(result)


# 책 코드
# n, m = map(int, input().split())
# result = 0

# for i in range(n):
#     data = list(map(int, input().split()))
#     min_value = min(data)
#     result = max(result, min_value)
# print(result)