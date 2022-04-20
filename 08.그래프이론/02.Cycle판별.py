input_data = """
3 3
1 2
1 3
2 3
"""


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_find(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 노드(n)와 간선(e) 입력 받기
n, e = map(int, input().split())

# 초기화
parent = [0] * (n+1)

# 자기 자신을 부모 node로 설정
for i in range(1, n+1):
    parent[i] = i

Cycle = False

# 간선 정보(e) 입력 받기
for i in range(e):
    a, b = map(int, input().split())

    # cycle 발생한 경우 종료
    if find_parent(parent, a) == find_parent(parent, b):
        Cycle = True
        break
    else:
        union_find(parent, a, b)

if Cycle:
    print("Cycle이 발생하였습니다.")
else:
    print("Cycle이 발생하지 않았습니다.")
