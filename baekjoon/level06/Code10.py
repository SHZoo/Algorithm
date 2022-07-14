from sre_constants import CHCODES


n = int(input())
sum = 0

for i in range(n) :
    word = input()
    fail = 0
    check_list = []
    for j in range(len(word)) :
        if not (word[j] in check_list) :
            check_list.append(word[j])
        elif word[j] in check_list :
            if word[j] == word[j-1] :
                pass
            else :
                fail += 1
    if fail == 0 :
        sum += 1

print(sum)