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
