import sys 
n = int(sys.stdin.readline())
run_time = list(map(int,sys.stdin.readline().split()))
run_time.sort()
waiting_time = run_time.copy()
sum = 0
for i in run_time :
    sum += i*len(waiting_time)
    waiting_time.pop(0)

print(sum)