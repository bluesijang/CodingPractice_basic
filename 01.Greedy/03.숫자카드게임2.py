# n(행) * m(열)
# 뽑고자하는 카드가 포함되어 있는 행 선택
# 행에서 가장 작은 숫자 뽑기 (1개 in 1행)
# 마지막 뽑은 카드 숫자가 가장 높도록 해야 함

# 1 <=n, m <= 100
# 2째줄 입력 : n개의 줄에 걸쳐 각 카드에 적힌 숫자 입력
# 카드 숫자 1~10,000
# 마지막에 선택된 카드에 적힌 숫자 출력하기


n, m = map(int, input().split())

cards = []
max_num = 0

for _ in range(n):
    cards = list(map(int, input().split()))

    if max_num < min(cards):
        max_num = min(cards)

print(max_num)

# card for loop을 입력 for loop 에 같이 넣을 수 있음
