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
for i in range(1, n+1):
    parent[i] = i


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 모든 원소를 check하지 않음 (input data만.. => 일부 root node만 찾음 => 부모 node로 볼 수 있음)
def union_find(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(m):
    a, b = map(int, input().split())
    union_find(parent, a, b)

# 모든 원소를 check (root node를 찾음)
print("각 원소가 속한 집합 : ", end=' ')
for i in range(1, n+1):
    print(find_parent(parent, i), end=' ')

print()
print("부모 테이블 : ", parent)
