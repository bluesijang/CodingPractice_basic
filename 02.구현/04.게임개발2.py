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
a, b, direction = map(int, input().split())

map_table = [[0] * m for _ in range(n)]

for i in range(n):
    map_table[i] = list(map(int, input().split()))

# visited = [[0] * m] * n
visited = [[0] * m for _ in range(n)]
visited[a][b] = 1

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def Turn_Left():
    global direction
    direction = 3 if direction-1 == -1 else direction - 1


count = 1
turn_time = 0

while True:
    Turn_Left()
    nx = a + dx[direction]
    ny = b + dy[direction]
    if visited[nx][ny] == 0 and map_table[nx][ny] == 0:
        visited[nx][ny] = 1
        a, b = nx, ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = a - dx[direction]
        ny = b - dy[direction]

        if map_table[nx][ny] == 0:
            a, b = nx, ny
        else:
            break
        turn_time = 0


print(">> Count : ", count)
