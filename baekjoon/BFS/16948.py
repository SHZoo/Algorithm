# boj 16948 데스 나이트
import heapq

n = int(input())
x1, y1, x2, y2 = map(int, input().split())
dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]
dict = {}

def bfs(x, y):
    hq = []
    heapq.heappush(hq, (0, x, y))

    while hq:
        cnt, x, y = heapq.heappop(hq)
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if (nx, ny) in dict:
                continue
            dict[(nx, ny)] = 1
            if (nx, ny) == (x2, y2):
                return cnt+1
            heapq.heappush(hq, (cnt+1, nx, ny))
    return None

res = bfs(x1, y1)

if res == None:
    print(-1)
else:
    print(res)