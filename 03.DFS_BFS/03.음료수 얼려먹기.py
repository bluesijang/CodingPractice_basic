# input - 1st line : 세로 n, 가로 m
#         2~n+1 line : n * m data
# 0 구멍, 1 막힌 곳


# n, m = map(int, input().split())
from pyrsistent import v


n, m = 4, 5

# for _ in range(n):
#     m = list(map(int, input().split()))

graph = [
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
]


visited = [[0] * m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    global graph
    global visited

    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if visited[x][y] == 0 and graph[x][y] == 0:
        visited[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


def bfs(graph, v, visited):
    pass


count = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            count += 1


print(count)
