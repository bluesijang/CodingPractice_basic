import sys

input = sys.stdin.readline
INF = int(1e9)
# n, m = map(int, input().split())
# start = int(input())

# n : node
# m : line numbers from node to node
n, m = 6, 11
start = 1

graph = [[] for _ in range(n+1)]    # from, to, 거리
visited = [False] * (n+1)           # 방문처리
distance = [INF] * (n+1)            # 최단거리

# copy & paste into console
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

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for i in graph[start]:
        distance[i[0]] = i[1]

    # start를 제외한 node 수
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True

        # 현재 node와 연결된 다른 node 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost


dijkstra(start)
print("*"*50)
for i in range(1, n+1):
    if distance[i] == INF:
        print(f"node {i}: Infinity")
    else:
        print(f"node {i}:", distance[i])
