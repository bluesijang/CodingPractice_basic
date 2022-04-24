# 강의 수 n (병렬 수강 가능, 우선순위 없을 때)
# 강의 번호, 선수 강의 번호(마지막은 -1)

# 1~n 각 강의까지의 최소 수강시간을 구하시오

from collections import deque
import copy


input_data = """
5 
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
"""
n = int(input())

# 진입 차수
ingress = [0] * (n+1)
graph = [[] for _ in range(n+1)]

# 강의 시간
LectureTime = [0] * (n+1)

for i in range(1, n+1):
    data = list(map(int, input().split()))

    LectureTime[i] = data[0]

    print("data / data[1:-1] :", data, "/", data[1:-1])
    for x in data[1:-1]:
        ingress[i] += 1
        graph[x].append(i)
        print("[graph/x/i] : ", x, "/", i, "/", graph)

print("=============data=============")
for i in data:
    print(i)

print("=============graph=============")
for i in graph:
    print(i)

print("=============LectureTime=============")
for i in LectureTime:
    print(i)


def topology():
    result = copy.deepcopy(LectureTime)
    q = deque()

    # 진입 차수가 0
    for i in range(1, n+1):
        if ingress[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()

        for i in graph[now]:
            result[i] = max(result[i], result[now] + LectureTime[i])
            ingress[i] -= 1
            if ingress[i] == 0:
                q.append(i)

    for i in range(n+1):
        print(result[i])


# topology()
