# 첫 줄 떡의 개수 n과 요청한 떡의 길이 m이 주어진다
# 1 <= n <= 1 * 10^6
# 1 <= m <= 2 * 10^9
# 둘째줄은 떡의 개별 높이(0 ~ 10억)

# m개만큼 갖고가기 위한 절단기 설정의 최대 높이값을 구하시오

n, m = 4, 6
height = [19, 15, 10, 17]
# n, m = map(int, input().split())
# height = list(map(int, input().split()))

start = 0
end = max(height)
result = 0

height.sort()

while start <= end:
    mid = (start + end) // 2
    sum = 0

    for i in height:
        # if i > mid:
        #     sum += i - mid
        sum += (i - mid if i - mid >= 0 else 0)

    if sum >= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(mid, m, sum, result)
