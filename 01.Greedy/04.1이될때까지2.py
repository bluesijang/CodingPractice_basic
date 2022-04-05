# 1이 될 때까지 다음 아래 두 과정중 하나를 반복
#   n - 1
#   n - k
# 1이 될 때까지 최소 횟수 구하기
#
# 입력 : 2 <= n, k <= 100,000

n, k = map(int, input().split())

result = 0

while n >= k:
    target = (n // k) * k
    result += (n - target)
    n = target
    if n < k:
        break
    n //= k
    result += 1

result += (n-1)     # 1이 될 때까지.. 1은 제외
print(result)
