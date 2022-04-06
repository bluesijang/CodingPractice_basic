# 8*8 체스판에서(1,1)~(8,8) 좌표가 주어질 때 knight가 움직일 수 있는 경우의 수 구하기
# 행(a~h), 열(1~8)
# 입력 1st line 예시 : a1 (행+열 순서로)

a = input()

y = list('abcdefgh').index(a[0]) + 1
x = int(a[1])
steps = [(2, 1), (2, -1), (-2, 1), (-2, -1),
         (1, 2), (-1, 2), (1, -2), (-1, -2)]

count = 0

for step in steps:
    nx = x + step[0]
    ny = y + step[1]
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        count += 1

print(count)
