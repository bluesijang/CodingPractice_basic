# n 가지 종류의 화폐 (1 line input)
# 화폐의 합 m (2 line input)
# 1 <= n <= 100, 1 <= m <= 10,000

# 최소의 화폐수로 구성할 수 있는 수, 없을 경우 -1
n, m = map(int, input().split())
kind = []
for _ in range(n):
    kind.append(int(input()))

d = [10001] * (m+1)

d[0] = 0

for i in range(n):
    for j in range(kind[i], m+1):
        if d[j - kind[i]] != 10001:
            d[j] = min(d[j], d[j - kind[i]] + 1)

if d[m] != 10001:
    print(d[m])
else:
    print(-1)
