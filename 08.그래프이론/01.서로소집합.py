# 1st line : num of nodes(n), input data(m)
# 2 ~ m+1 line : node to node connection

# output
# 각 원소가 속한 집합 : O, O, O, O, O,
# 부모테이블 : O, O, O, O, O

n, m = map(int, input().split())

input_data = """
6 4
1 4
2 3
2 4
5 6
"""

# 부모 테이블 초기화
parent = [0] * (n+1)

# 자기 자신을 parent로 설정
parent = [i for i in range(n+1)]


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


for _ in range(m):
    a, b = map(int, input().split())
    union_parent(parent, a, b)


print("부모 테이블 : ", parent)
