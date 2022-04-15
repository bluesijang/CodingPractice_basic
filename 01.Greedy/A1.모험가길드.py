n = int(input())
array = list(map(int, input().split()))

cnt = 0
sum = 0
idx = 0

array.sort(reverse=True)

while sum < n:
    sum += array[idx]
    cnt += 1

print(cnt)
