# 입력 금액에 대해 최소한의 거스름돈의 수
N = int(input("금액 : "))


result = 0

if N // 500 > 0:
    result += N // 500
    N = N % 500

if N // 100 > 0:
    result += N // 100
    N = N % 100

if N // 50 > 0:
    result += N // 50
    N = N % 50

if N // 10 > 0:
    result += N // 10
    N = N % 10

print(result)
