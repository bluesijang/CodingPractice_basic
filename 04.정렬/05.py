n = int(input())
data = []
for _ in range(n):
    x, y = input().split()
    y = int(y)
    data.append((x, y))

result = sorted(data, key=lambda x: x[1])

for i in result:
    print(i[0], end=" ")
