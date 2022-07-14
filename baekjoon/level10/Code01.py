import sys
n, m = map(int, sys.stdin.readline().split())
card_list = []
blackjack_list = []

card_list.extend(list(map(int, sys.stdin.readline().split())))

for i in range(0, n-2) :
    for j in range(i, n-2) :
        if i == n-2 :
            j = i
        for k in range(j, n-2) :
            if j == n - 2 :
                k = j
                sum = card_list[0+i] + card_list[1+j] + card_list[2+k]
                blackjack_list.append(sum)
            else :
                sum = card_list[0+i] + card_list[1+j] + card_list[2+k]
                blackjack_list.append(sum)

blackjack_list = list(filter(lambda x : x <= m, blackjack_list))
if len(blackjack_list) != 0 :
    print(max(blackjack_list))