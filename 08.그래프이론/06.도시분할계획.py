# n개의 집, m개의 길
# m개의 길 => a번집, B번집, 길 유지비 c
# 2개로 분리할 때 남는 유지비 합의 최소값
input_data = """
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
"""

n, m = map(int, input().split())
parent = [0] * (n+1)


for i in range(n+1):
    parent[i] = i


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


edges = []

for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()
result = 0
last = 0  # 마지막(제일큰 due to sorting) 비용

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_find(parent, a, b)
        result += cost
        last = cost


print(result - cost)
