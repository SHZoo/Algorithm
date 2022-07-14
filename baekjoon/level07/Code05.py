import sys
import math
t = int(sys.stdin.readline())
for _ in range(t) :
    h, w, n = map(int, sys.stdin.readline().split())

    if n % h == 0 :
        floor = h 
    else :
        floor = n % h

    line = math.ceil(n/h)

    if line < 10 :
        line = '0' + str(line)
    else :
        line = str(line)

    print(str(floor) + line)

