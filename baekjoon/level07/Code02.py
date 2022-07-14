import sys
input_num = int(sys.stdin.readline())

new_list = []
start_num = 1
acc = 6
cnt = 1
while input_num > start_num :
    start_num += acc
    acc += 6
    cnt += 1
    

print(cnt)