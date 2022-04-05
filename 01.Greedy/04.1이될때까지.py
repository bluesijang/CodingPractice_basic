# 1이 될 때까지 다음 아래 두 과정중 하나를 반복
#   n - 1
#   n - k
# 1이 될 때까지 최소 횟수 구하기
#
# 입력 : 2 <= n, k <= 100,000

n, k = map(int, input().split())

result = 0

while n - k >= 0:
    while n != 1:
        if n % k == 0:
            n = n // k
        else:
            n -= 1
        result += 1

while n > 1:
    n -= 1
    result += 1

print(result)
