n = int(input())
for i in range(n) :
    r, str = input().split()
    r = int(r)
    text = ""
    for j in str :
        text += j*r
    print(text)