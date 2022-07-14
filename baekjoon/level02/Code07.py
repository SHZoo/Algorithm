a, b, c = map(int,input().split())
if a == b == c :
    print(10000 + a * 1000)
elif ( a == b != c) or ( a == c != b) :
    print(1000 + a * 100)
elif ( a != b == c ) :
    print(1000 + c * 100 )
else :
    if a > b and a > c :
        print(100 * a)
    elif b > a and b > c :
        print(100 * b)
    elif c > a and c > b :
        print(100 * c)