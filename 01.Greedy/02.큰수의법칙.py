# n : 배열을 크기 (2번째 입력 줄) ( 2 < n < 1,000)
# m : 숫자가 더해지는 횟수  ( 0 < m < 10,000)
# k : 같은 index의 덧셈의 max 반복 횟수 ( 0 < k < 10,000)

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
    if inc == k:
        inc = 0
        sum += second2max
    else:
        sum += first2max

print(sum)

# 위 방식으로 할 때 m의 크기가 100억 이상처럼 커질 경우 시간 초과 발생
# => 반복되는 수열의 파악이 필요함
# [6,6,6,5] + [6,6,6,5] + ...
# max 값 반복 회수 : int(m//(k+1)) * k + m % (k + 1)  => 이 방법으로 다시 풀어보기
