
n = int(input("금액 입력 : "))
coins = [500, 100, 50, 10]

count = 0

for coin in coins:
    count += n // coin
    n %= coin

print(count)
