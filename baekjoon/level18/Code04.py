import sys
str = sys.stdin.readline().strip()
list_int = []
list_operator = []
init = ''
for i in range(len(str)) :
    try :
        a = int(str[i])
        init += str[i]
        if i == len(str) - 1 :
          list_int.append(int(init))  
    except : 
        list_operator.append(str[i])
        list_int.append(int(init))
        init = ''
sum = 0
sum_minus = 0
for i in range(len(list_int)) :
    if i == 0 :
        sum += list_int[i]
    else :
        if list_operator[i-1] == '+' and sum_minus == 0 :
            sum += list_int[i]
        elif list_operator[i-1] == '-' and sum_minus == 0 :
            sum_minus = 1
            sum -= list_int[i]
        elif list_operator[i-1] == '+' and sum_minus == 1 :
            sum -= list_int[i]
        elif list_operator[i-1] == '-' and sum_minus == 1 :
            sum -= list_int[i]

print(sum)