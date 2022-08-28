# boj 12851 숨바꼭질2
from collections import deque

n, k = map(int, input().split())
visited = [1e9] * 100001

def bfs(start, k):
    queue = deque([(start, 0)])
    res = 0
    cnt_low = 1e9

    while queue:
        now, cnt = queue.popleft()
        if now == k and cnt <= cnt_low:
            cnt_low = cnt
            res += 1
        if cnt >= cnt_low:
            continue
        if now+1 <= 100000 and cnt <= visited[now+1]:
            queue.append((now+1, cnt+1))
            visited[now+1] = cnt
        if now*2 <= 100000 and cnt <= visited[now*2]:
            queue.append((now*2, cnt+1))
            visited[now*2] = cnt
        if now-1 >= 0 and cnt <= visited[now-1]:
            queue.append((now-1, cnt+1))
            visited[now-1] = cnt
    return cnt_low, res

res_1, res_2 = bfs(n, k)
print(res_1, res_2, sep = '\n')