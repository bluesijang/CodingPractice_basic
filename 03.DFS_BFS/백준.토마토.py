# https://www.acmicpc.net/problem/7576

from collections import deque

m, n = map(int, input().split())
graph = []
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]



visited = [[0] * m for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, input().split())))

input_data = """
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
"""


q = deque()

is_ripe = False

# FIXME: 1이 두개가 있는것이 있음
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            start = (i, j)
            is_ripe = True
            break


if not is_ripe:
    if min(min(graph)) == 0:
        print(0)
    else:
        print(-1)
else:
    q.append((start[0], start[1]))
    while q:
        x, y = q.popleft()
        visited[x][y] = 1

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny] !=0 or graph[nx][ny] !=0:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                is_ripe = False
    if is_ripe:
        print(max(max(graph)) - 1)
        for i in graph:
            print(i)
    else:
        print(-1)




#
# for i in visited:
#     print(i)
# print("=====================")
# for i in graph:
#     print(i)
