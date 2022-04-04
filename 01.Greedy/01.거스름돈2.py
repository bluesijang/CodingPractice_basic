# 입력 금액에 대해 최소한의 거스름돈의 수

n = int(input("금액 입력 : "))
coins = [500, 100, 50, 10]

count = 0

for coin in coins:
    count += n // coin
    n %= coin

print(count)
