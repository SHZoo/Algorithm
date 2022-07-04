numbers = [1, 2, 3, 4, 5]
iterator = reversed(numbers)

 # 메모리를 절약할 수 있다.
for i in iterator :
    print(i)

for i in iterator :
    print(i)

for i in iterator :
    print(i)

def 반전(리스트) :
    for i in range(len(리스트)):
        yield 리스트[-i -1]
    
반전([1, 2, 3, 4, 5, 6])

