import sys
string = sys.stdin.readline().strip()
cnt = 0
s_1 = set()

for i in range(0, len(string)) :
    for j in range(i+1, len(string)+1) :
        s_1.add(string[i:j])
    
print(len(s_1))
