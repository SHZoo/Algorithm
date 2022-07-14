import sys
n = int(sys.stdin.readline())
distance_list = list(map(int, sys.stdin.readline().split()))
cost_list = list(map(int, sys.stdin.readline().split()))
distance = 0
sum = 0
result = 0


for i in range(n) :
    if i == 0 :
        cost = cost_list[i] 
        sum += distance_list[i]
    elif i == n - 1 :
            result += sum * cost
            break
    else :
        if cost < cost_list[i] :
            sum += distance_list[i]
        
        else :
            result += cost * sum
            sum = 0
            cost = cost_list[i]
            sum += distance_list[i]

print(result)
