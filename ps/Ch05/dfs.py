# 깊이 우선 탐색(Depth First Search)
def dfs(graph, v, visited) :
    visited[v] = True
    print(v, end = ' ')
    for i in graph[v] :
        if not visited[i] :
            dfs(graph, i, visited)

graph = [
    [], # 제로 인덱스용
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False for _ in range(9)] 

dfs(graph, 1, visited)