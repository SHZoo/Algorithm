# 내 코드 
input_data = input()
x = int(input_data[1])
y = int(ord(input_data[0])) - int(ord("a")) + 1
move_types = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
cnt = 0

for i in move_types :
    nx = x + i[0]
    ny = y + i[1]

    if 1 <= nx <= 8 and 1 <= ny <= 8 :
        cnt += 1

print(cnt)

