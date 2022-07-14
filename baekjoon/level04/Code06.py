n = int(input())
for i in range(n) :
    input_text = input()
    cnt = 0
    acc = 0
    for j in input_text :
        if j == "O" :
            acc += 1
            cnt += acc
        else :
            acc = 0
    print(cnt)