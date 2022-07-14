import sys
a = int(sys.stdin.readline())
for i in range(a , 0, -1) :
    print(" " * (i-1) + "*" * (a - i + 1))