# 1182 부분수열의 합
n, s = map(int, input().split())
array = list(map(int, input().split()))
res = 0

def dfs(idx, sum) :
    global res 
    if idx >= n :
        return
    sum += array[idx]
    if (sum == s) :
        res += 1
    dfs(idx+1, sum-array[idx])
    dfs(idx+1, sum)

dfs(0, 0)
print(res)