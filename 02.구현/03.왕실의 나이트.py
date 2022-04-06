# 8*8 체스판에서(1,1)~(8,8) 좌표가 주어질 때 knight가 움직일 수 있는 경우의 수 구하기
# 행(a~h), 열(1~8)
# 입력 1st line 예시 : a1 (행+열 순서로)

a = input()

y = list('abcdefgh').index(a[0]) + 1
x = int(a[1])
dx = [2, 2, -2, -2, 1, -1, 1, -1]
dy = [1, -1, 1, -1, 2, 2, -2, -2]

count = 0

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 1 or nx > 8 or ny < 1 or ny > 8:
        continue
    count += 1

print(count)
