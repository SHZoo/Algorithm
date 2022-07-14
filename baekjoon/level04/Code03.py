first_number = int(input())
second_number = int(input())
third_number = int(input())
product = str(first_number * second_number * third_number)

num0 = 0
num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0
num6 = 0
num7 = 0
num8 = 0
num9 = 0

for i in product :
    if i == "0" :
        num0 += 1
    elif i == "1" :
        num1 += 1
    elif i == "2" :
        num2 += 1
    elif i == "3" :
        num3 += 1
    elif i == "4" :
        num4 += 1
    elif i == "5" :
        num5 += 1
    elif i == "6" :
        num6 += 1
    elif i == "7" :
        num7 += 1
    elif i == "8" :
        num8 += 1
    elif i == "9" :
        num9 += 1
print(num0, num1, num2, num3, num4, num5, num6, num7, num8, num9, sep = "\n")



