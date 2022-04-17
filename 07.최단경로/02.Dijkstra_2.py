# priority queue (heapq, min heap) 사용

import heapq
import sys

# n, m = map(int, input().split())
# start = int(input())
INF = int(1e9)

n, m = 6, 11
start = 1

graph = [[] for _ in range(n+1)]

# node a to node b distance is c
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

distance = [INF] * (n+1)

input_graph_data = """
1	2	2
1	3	5
1	4	1
2	3	3
2	4	2
3	2	3
3	6	5
4	3	3
4	5	1
5	3	1
5	6	2
"""


def dijkstra(start):
    h = []
    distance[start] = 0
    heapq.heappush(h, (0, start))

    while h:
        dist, now = heapq.heappop(h)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(h, (cost, i[0]))


dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print(f"{i} : INFINITY")
    else:
        print(f"{i} :", distance[i])
