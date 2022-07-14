str = input()
exam = 'abcdefghijklmnopqrstuvwxyz'
test_list = []
for i in exam :
    if i in str :
        test_list.append(str.find(i))
    else :
        test_list.append(-1)

for i in test_list :
    print(i, end = " ")