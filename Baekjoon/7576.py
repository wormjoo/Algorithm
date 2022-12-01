from collections import deque

m, n = map(int, input().split())
tomatoes = []
day = 0
queue = deque()

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

for _ in range(n):
    tomatoes.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if tomatoes[i][j] == 1:
            queue.append((i, j))


while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        else:
            if tomatoes[nx][ny] == 0:
                tomatoes[nx][ny] = tomatoes[x][y] + 1
                queue.append((nx, ny))
                
isRipe = True

for i in range(n):
    for j in range(m):
        if tomatoes[i][j] == 0:
            isRipe = False
            break

if isRipe:
    print(max(map(max, tomatoes)) - 1)
else:
    print(-1)
