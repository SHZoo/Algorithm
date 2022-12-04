a = input()
a = a.replace("XXXX", "AAAA")
a = a.replace("XX", "BB")
if a.count('X') >= 1:
    a = -1
print(a)
