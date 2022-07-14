new_list = []
cnt = 0
for _ in range(10) :
    num = int(input())
    rest = num % 42
    if not (rest in new_list) :
        new_list.append(rest)

print(len(new_list))
        
