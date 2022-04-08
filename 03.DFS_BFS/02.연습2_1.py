from collections import deque

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [0]*len(graph)

i = 1
queue = deque([])
queue.append(i)
visited[1] = 1

while queue:

    q = queue.popleft()
    print(q, end=' ')

    for i in graph[q]:
        if visited[i] == 0:
            queue.append(i)
            visited[i] = 1
