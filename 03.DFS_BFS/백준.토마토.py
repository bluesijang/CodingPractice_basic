# https://www.acmicpc.net/problem/7576

from collections import deque

m, n = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
visited = [[0] * m for _ in range(n)]

def bfs(x, y):
    global graph
    global visited
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny] == 1:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))

    # FIXME:
    return max(max(graph)) - 1


MaxDays = 0
is_processed = False
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            is_processed = True
            a = bfs(i, j)
            if MaxDays < a:
                MaxDays = a

if is_processed:
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                is_processed = False
                break
    if is_processed:
        print(MaxDays)
    else:
        print(-1)
else:
    SomeExist = False
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                SomeExist = True
                break

    if SomeExist:
        print(0)
    else:
        print(-1)


for i in graph:
    print(i)
