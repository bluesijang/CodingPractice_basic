# 1~N번 회사가 있고, 회사들은 도로를 통해 연결되어 있음
# 판매원 A는 1번 회사위치에 있고, X번 회사에 방문해 물건을 팔려고 함
# 연결 도로는 양방향 / 1시간 거리
# X 회사를 가기 전 K 회사를 방문 후 X 회사에 도착

# 1st : 1 <= 회사수 n, 경로 수 m <= 100
# 2nd : m 정보
# 마지막줄 : 거쳐갈 x와 최종 목적지 K (X, K)
# 방문원 A가 K를 거처 X로 가는 최소 이동시간을 구하시오

# copy & paste
input_data1 = """
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
"""
input_data2 = """
4 2
1 3
2 4
3 4
"""
n, m = map(int, input().split())
INF = int(1e9)

graph = [[INF] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for t in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][t]+graph[t][b])

distance = graph[1][k] + graph[k][x]

for i in graph:
    print(i)

if distance >= INF:
    print(-1)
else:
    print(distance)
