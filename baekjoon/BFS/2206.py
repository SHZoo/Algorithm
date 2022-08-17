# boj 2206
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
queue = deque([(0, 0, 0)])

def bfs() :
    visit = [[[0]*2 for _ in range(m)] for _ in range(n)] # visit 3차원 배열
    visit[0][0][0] = 1

    while queue :
        x, y, state = queue.popleft()
        if (x, y) == (n-1, m-1) :
            return visit[x][y][state]
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m :
                continue
            if visit[nx][ny][state] == 0 :   # 벽을 부쉈든 안 부쉈든 아직 해당 장소에 방문 안 함
                if graph[nx][ny] == 0 : # 해당 장소가 길이라면
                    visit[nx][ny][state] = visit[x][y][state] + 1
                    queue.append((nx, ny, state))
                elif state == 0 and graph[nx][ny] == 1 : # 아직 벽을 안 부쉈고 해당 장소가 벽이라면
                    visit[nx][ny][1] = visit[x][y][0] + 1
                    queue.append((nx, ny, 1))
    return -1

print(bfs())