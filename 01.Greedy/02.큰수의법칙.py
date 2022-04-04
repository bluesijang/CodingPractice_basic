# n : 배열을 크기 (2번째 입력 줄)
# m : 숫자가 더해지는 횟수
# k : 같은 index의 덧셈의 max 반복 횟수
from socket import send_fds


n, m, k = map(int, input().split())

arr = list(map(int, input().split()))

print(n, m, k)
print(arr)

arr.sort()
first2max = arr[n-1]
second2max = arr[n-2]
sum = 0
inc = 0

for i in range(m):
    inc += 1
    if (inc + 1) == k:
        inc = 0
        sum += second2max
    else:
        sum += first2max

print(sum)
