# 0 ~ n 명 학생, 8개 data
# 0 ? ? : 팀 합치기
# 1 ? ? : 같은 팀 여부 확인

# 1 ? ? 연산에 대한 결과를 YES/NO로 출력하시오

input_data = """
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
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


for i in range(m):
    x, a, b = map(int, input().split())
    if x == 0:
        union_find(parent, a, b)
    elif x == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")
