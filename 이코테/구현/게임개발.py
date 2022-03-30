n, m = map(int, input().split())
x, y, d = map(int, input().split())
board = [[0]*m for i in range(n)]
board[x][y] = 1
count = 1
turn = 0
arr = []

for i in range(m):
    arr.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while True:
    d -= 1
    if d == -1:
        d = 3
    nx = x + dx[d]
    ny = y + dy[d]
    if board[nx][ny] == 0 and arr[nx][ny] == 0:
        board[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn = 0
        continue
    else:
        turn += 1
    if turn == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        if arr[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn = 0

print(count)