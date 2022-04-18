# n개의 도시가 있다
# X -> Y 도시로 연결(방향성 있음) 정보가 있다
# C도시에서 위급사항이 발생했을 때 보낸 메세지를 받게되는 최대 도시 수를 구하시오

# 1st : 도시의 개수n, 통로의 개수m, 메세지를 보내고자 하는 도시 C
#       1<=n<=30,000    1<=m<=200,000   1<=c<=n
# 2nd ~ m+1줄 : 통로에 대한 정보 x, y, z
#               x → Y도시로 전달시간은 z
# output : C가 보낸 메세지를 받는 도시의 총 개수와 총 걸리는 시간을 공백으로 구분하여 출력하시오

import heapq

input_data1 = """
3 2 1
1 2 4
1 3 2
"""
n, m, start = map(int, input().split())
INF = int(1e9)
distance = [INF] * (n+1)
graph = [[] for _ in range(n+1)]


for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))   # heapq (distance, node)
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        print(f"dist, now :{dist}, {now}")
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

print(graph)
print(distance)

count = 0
max_value = 0

for i in distance:
    if i != INF:
        count += 1
        if max_value < i:
            max_value = i

print(count-1, max_value)
