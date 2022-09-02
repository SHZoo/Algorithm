# boj 7562 나이트의 이동
from collections import deque

t = int(input())
dx = [2, 2, 1, 1, -1, -1, -2, -2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]

def bfs(x, y, des_x, des_y):
    queue = deque([(x, y, 0)])

    while queue:
        x, y, cnt = queue.popleft()
        if (x, y) == (des_x, des_y):
            return cnt
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if (nx, ny) in dict:
                continue
            dict[(nx, ny)] = 1
            queue.append((nx, ny, cnt+1))

for _ in range(t):
    n = int(input())
    dict = {}
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    print(bfs(x1, y1, x2, y2))