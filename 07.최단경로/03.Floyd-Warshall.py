# first line => n : n*n matrix
# second line => m : input data numbers
# Find optimized path for all node by using Floyd-Warshall Algorithm

# n = int(input())
# m = int(input())

n, m = 4, 7
INF = int(1e9)

# copy & paste
input_data = """
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
"""

# initialization
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c


for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


print("*"*50)
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print("INF", end=' ')
        else:
            print(graph[i][j], end=' ')

    print()
