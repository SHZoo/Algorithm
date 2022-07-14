import sys
cnt = 0
def hansu(n) :
    global cnt 
    if len(str(n)) == 1 or len(str(n)) == 2 :
        cnt += 1
    elif len(str(n)) == 3 :
        if int(str(n)[2]) - int(str(n)[1]) == int(str(n)[1]) - int(str(n)[0]) :
            cnt += 1
    
n = int(sys.stdin.readline())
if n == 1 :
    print(1)
else:
    for i in range(1, n + 1) :
        hansu(i)
    print(cnt)

