test_word = input().lower()
alpha = "abcdefghijklmnopqrstuvwxyz"
list_test = []
for i in alpha :
    cnt = 0
    if i in test_word :
        for j in test_word :
            if i == j :
                cnt += 1
        if len(list_test) == 0:
            list_test.append((i, cnt))
        elif len(list_test) > 0 and cnt > list_test[0][1] :
            list_test.clear()
            list_test.append((i, cnt))
        elif len(list_test) > 0 and cnt == list_test[0][1] :
            list_test.append((i, cnt))

if len(list_test) == 1 :
    print(list_test[0][0].upper())
else :
    print("?")