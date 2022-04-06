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
x, y = 1, 1
nx, ny = 0, 0

for operation in operations:
    for i in range(len(direction)):
        if operation == direction[i]:
            ny = y + dy[i]
            nx = x + dx[i]

    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    y, x = ny, nx

print(f"{x} {y}")
