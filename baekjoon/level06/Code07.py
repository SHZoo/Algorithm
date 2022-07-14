a, b = input().split()
c = ""
d = ""

for i in range(-1, -4, -1) :
     c += a[i]

for i in range(-1, -4, -1) :
     d += b[i]
    
c = int(c)
d = int(d)

if c > d :
    print(c)
else :
    print(d)