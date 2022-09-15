# boj 4677 Oil Deposits
def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    if graph[x][y] == '@':
        graph[x][y] = '*'
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        dfs(x - 1, y - 1)
        dfs(x + 1, y + 1)
        dfs(x - 1, y + 1)
        dfs(x + 1, y - 1)
        return True
    return False


while True:
    n, m = map(int, input().split())
    if (n, m) == (0, 0):
        break
    graph = []
    res = 0

    for _ in range(n):
        graph.append(list(input()))

    for i in range(n):
        for j in range(m):
            if graph[i][j] == '@':
                res += 1
                dfs(i, j)

    print(res)