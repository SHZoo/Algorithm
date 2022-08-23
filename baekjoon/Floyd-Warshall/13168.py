# boj 13168 내일로 여행
import sys

input = sys.stdin.readline
INF = (1e9)
n, r = map(int, input().split())
dict_1 = {'Mugunghwa' : 0, 'ITX-Saemaeul' : 0, 'ITX-Cheongchun' : 0, 'S-Train' : 1, 'V-Train' : 1, 'Subway' : 2, 'Bus' : 2, 'Taxi' : 2, 'Airplane' : 2, 'KTX' : 2}
dict_2 = {}
graph_1 = [[INF] * (n+1) for _ in range(n+1)] # 내일로 X
graph_2 = [[INF] * (n+1) for _ in range(n+1)] # 내일로 O

city_list = list(input().strip().split())
i = 1
for city in city_list :
    if city not in dict_2 :
        dict_2[city] = i
        i += 1

m = int(input())
tour_list = list(input().strip().split())

k = int(input())
for _ in range(k) :
    input_data = input().strip().split()
    graph_1[dict_2[input_data[1]]][dict_2[input_data[2]]] = min(graph_1[dict_2[input_data[1]]][dict_2[input_data[2]]], float(input_data[3]))
    graph_1[dict_2[input_data[2]]][dict_2[input_data[1]]] = min(graph_1[dict_2[input_data[2]]][dict_2[input_data[1]]], float(input_data[3]))
    if dict_1[input_data[0]] == 0 :
        graph_2[dict_2[input_data[1]]][dict_2[input_data[2]]] = 0
        graph_2[dict_2[input_data[2]]][dict_2[input_data[1]]] = 0       
    elif dict_1[input_data[0]] == 1 :
        graph_2[dict_2[input_data[1]]][dict_2[input_data[2]]] = min(graph_2[dict_2[input_data[1]]][dict_2[input_data[2]]], float(input_data[3]) / 2) 
        graph_2[dict_2[input_data[2]]][dict_2[input_data[1]]] = min(graph_2[dict_2[input_data[2]]][dict_2[input_data[1]]], float(input_data[3]) / 2)      
    else :
        graph_2[dict_2[input_data[1]]][dict_2[input_data[2]]] = min(graph_2[dict_2[input_data[1]]][dict_2[input_data[2]]], float(input_data[3]))
        graph_2[dict_2[input_data[2]]][dict_2[input_data[1]]] = min(graph_2[dict_2[input_data[2]]][dict_2[input_data[1]]], float(input_data[3]))

for k in range(1, n+1) :
    for i in range(1, n+1) :
        for j in range(1, n+1) :
            graph_1[i][j] = min(graph_1[i][j], graph_1[i][k] + graph_1[k][j])
            graph_2[i][j] = min(graph_2[i][j], graph_2[i][k] + graph_2[k][j])

res_1 = 0
res_2 = r

for i in range(len(tour_list) - 1) :
    res_1 += graph_1[dict_2[tour_list[i]]][dict_2[tour_list[i+1]]]
    res_2 += graph_2[dict_2[tour_list[i]]][dict_2[tour_list[i+1]]]

if res_1 > res_2 :
    print('Yes')
else :
    print('No')