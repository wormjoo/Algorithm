n, m = map(int, input().split())
r, c, d = map(int, input().split())
board, current = [], [[0]*m for i in range(n)]
current[r][c] = 1
cnt = 1
turn = 0

for i in range(n):
    board.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while True:
    d -= 1
    if d == -1:
        d = 3
    x = r + dx[d]
    y = c + dy[d]
    if board[x][y] == 0 and current[x][y] == 0:
        current[x][y] = 1
        r = x
        c = y
        cnt += 1
        turn = 0
        continue
    else:
        turn += 1
    if turn == 4:
        x = r - dx[d]
        y = c - dy[d]
        if board[x][y] == 1:
            break
        else:
            r = x
            c = y
        turn = 0

print(cnt)
