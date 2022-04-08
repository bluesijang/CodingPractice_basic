# 총 크기 : n * m matrix, 각 tile은 바다 또는 육지이며 육지만 갈 수 있음
# 위치는 (a, b)로 나타냄
# 1) 현재 위치 기준으로 왼쪽 방향(반시계 방향으로 90' 회전한 방향)부터 차례대로 갈 곳을 정함
# 2) 왼쪽 방향에 아직 가보지 않은 칸이 있다면, 왼쪽으로 회전한 다음 왼쪽으로 한 칸을 전진하고
#    왼쪽 방향에 가 보았다면, 외쪽 방향으로 회전만하고 1단계로 돌아간다
# 3) 만약 모든 방향을 visited or if sea, 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다
#    이 때 뒷쪽이 바다이면 움직임을 멈춘다
#
# 총 방문한 칸의 수를 구하시오
# 1st line : n, m (3 <= n, m <= 50)
# 2nd line : 캐릭터 좌표 (A, B) 및 바라보는 방향 d  (서로 공백으로 구분)
#             d => 0(북쪽), 1(동쪽), 2(남쪽), 3(서쪽)
# 3rd line : n개의 줄에 북~남, 서~동쪽 방향으로 0: 육지, 1: 바다
#
# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1

def rotation(arr, direction):
    return arr[direction:] + arr[:direction]


n, m = map(int, input().split())
a, b, d = map(int, input().split())

map_table = [[0] * m for _ in range(n)]

for i in range(n):
    map_table[i] = list(map(int, input().split()))

visited = [[False] * m] * n

print("map table : ", map_table)

# 북 동 남 서
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# search direction
north = [(0, -1), (1, 0), (0, 1), (-1, 0)]      # 서 남 동 북
west = [(1, 0), (0, 1), (-1, 0), (0, -1)]      # 남 동 북 서
south = [(0, 1), (-1, 0), (0, -1), (1, 0)]      # 동 북 서 남
east = [(-1, 0), (0, -1), (1, 0), (0, 1)]    # 북 서 남 동

# 북 동 남 서
steps = [north, east, south, west]

# 0북 1동 2남 3서
backward = [(-1, 0), (0, 1), (1, 0), (0, 1)]
back = d - 4 if d + 2 > 3 else d + 2


blockedAll = 0
visited[a][b] = True
count = 1

# while blockedAll >= 4 and map_table[a+backward[back][0]][b+backward[back][1]] != 1:
while True:
    CurrentDirectionArrayIndex = d
    blockedAll = 0

    for i in range(3):
        nx = a + steps[CurrentDirectionArrayIndex][i][0]
        ny = b + steps[CurrentDirectionArrayIndex][i][1]

        if map_table[nx][ny] == 1 or visited[nx][ny] == True:
            continue

        if 0 <= nx < n and 0 <= ny < m and map_table[nx][ny] == 0 and visited[nx][ny] == False:
            visited[nx][ny] = True
            a, b = nx, ny
            d = d - i + 1 if d - i + 1 > 0 else d - i + 4
            count += 1
            break

        blockedAll += 1

    if blockedAll == 4:
        back = d - 4 if d + 2 > 3 else d + 2
        if map_table[a+backward[back][0]][b+backward[back][1]] == 1:
            break

print("Count >>> ", count)
