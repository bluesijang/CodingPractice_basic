# LRUD (left, right, up, down)
# n * n matrix
# Find final postion after LRUD given operations.

# start position : (1, 1)
# input : 1st line 1 <= n <= 1000
#         2nd line LRUD (~100)

n = int(input())
operations = [i.upper() for i in list(input().split())]
direction = ["L", "R", "U", "D"]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
x = y = 1
nx = ny = 0

for operation in operations:
    y += dy[direction.index(operation)]
    x += dx[direction.index(operation)]
    if x < 1 or x > n or y < 1 or y > n:
        y -= dy[direction.index(operation)]
        x -= dx[direction.index(operation)]

print(f"{x} {y}")
