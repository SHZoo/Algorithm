num = input()
sum = 0

for i in num : 
    if ord(i) <= 67 :
        sum += 3 
    elif ord(i) <= 70 :
        sum += 4
    elif ord(i) <= 73 :
        sum += 5
    elif ord(i) <= 76 :
        sum += 6
    elif ord(i) <= 79 :
        sum += 7
    elif ord(i) <= 83 :
        sum += 8
    elif ord(i) <= 86 :
        sum += 9
    elif ord(i) <= 90 :
        sum += 10
    else :
        sum += 2
        
print(sum)