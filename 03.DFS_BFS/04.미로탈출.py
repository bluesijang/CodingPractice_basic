from collections import deque

# n, m = map(int, input().split)

# graph = []
# for _ in range(n):
#     graph.append(list(map(int, input().split())))

n, m = 5, 6

graph = [
    [1, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1]
]

visited = [[0]*m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
