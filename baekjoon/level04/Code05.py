n = int(input())
list_max = list(map(int, input().split()))
max = max(list_max)
new_list = []
for i in list_max :
    new_list.append((100*i)/max)

avg = 0
for i in new_list :
    avg += i

avg = avg/len(new_list)
print(avg)