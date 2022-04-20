# 1) 진입차수가 0인 node를 queue에 넣는다
# 2) queue가 빌 때까지 다음의 과정을 반복한다.
#     i. queue에서 원소를 꺼내 해당 node의 출발간선을 제거
#     ii. 새로 진입차수가 0이 된 node를 queue에 넣기
#
# - 모든 원소를 방문하기 전 queue가 빈다면, cycle이 발생하는 것임
# - 위상 정렬은 DFS 또는 queue로 수행할 수도 있음
# - DAG(Direct Acyclic Graph) : cycle이 없는 방향 그래프

from collections import deque

input_data_sample = """
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4 
"""

# node 및 간선 입력
n, e = map(int, input().split())

# 진입차수 0으로 초기화
ingress = [0] * (n+1)

# 간선정보 graph 초기화
graph = [[] for _ in range(n+1)]

# 간선정보 입력
for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)      # move node a to b
    ingress[b] += 1         # ingress


def topology_sort():
    result = []
    q = deque()

    # ingress 가 없는 node (시작점)
    for i in range(1, n + 1):
        if ingress[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)      # node 를 삭제

        for i in graph[now]:    # 연결된 다음 node의
            ingress[i] -= 1     # 인입차수를 없애주고
            if ingress[i] == 0:  # 인입차수가 없다면
                q.append(i)

    # 위상정렬 결과
    for i in result:
        print(i, end=' ')


topology_sort()
