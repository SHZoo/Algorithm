import sys 

n, m = map(int, sys.stdin.readline().split())
dict = dict()
list_a = [0]
i = 1
for _ in range(n) :
    poketmon = sys.stdin.readline().strip()
    dict[poketmon] = i
    list_a.append(poketmon)
    i += 1

for i in range(m) :
    try :
        input_data = sys.stdin.readline().strip()
        input_data = int(input_data)
        print(list_a[input_data])
    except ValueError as e :
        print(dict[input_data])