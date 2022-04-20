# node 수, 입력 data 수
# 입력 데이터 node a, node b, cost
input_data_sample = """
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25
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


# node 와 edge 수 입력
n, e = map(int, input().split())

# 초기화
parent = [0] * (n+1)

# 자기자신 부모를 자기자신으로 설정
for i in range(1, n+1):
    parent[i] = i

edges = []

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

result = 0

# 비용순으로 간선 sorting
edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_find(parent, a, b)
        result += cost

print(result)
