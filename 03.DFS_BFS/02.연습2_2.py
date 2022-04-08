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

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        q = queue.popleft()
        print(q, end=' ')

        for i in graph[q]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


visited = [False] * len(graph)

bfs(graph, 1, visited)
