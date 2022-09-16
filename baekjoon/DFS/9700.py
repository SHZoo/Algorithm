# boj 9700 RAINFOREST CANOPY
import sys

sys.setrecursionlimit(10 ** 6)
case = 0


def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        dfs(x - 1, y - 1)
        dfs(x + 1, y - 1)
        dfs(x + 1, y + 1)
        dfs(x - 1, y + 1)
        return True
    return False


while True:
    try:
        case += 1
        graph = []
        res = 0
        n = int(input())

        for _ in range(n):
            graph.append(list(map(int, input())))

        for i in range(n):
            for j in range(n):
                if graph[i][j] == 1:
                    res += 1
                    dfs(i, j)
        print("Case #{}: {}".format(case, res))

    except:
        break