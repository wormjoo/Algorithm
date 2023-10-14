from collections import deque

n, m, k = map(int, input().split())
array = []
dice = [[0, 2, 0], [4, 1, 3], [0, 5, 0], [0, 6, 0]]
x = 0
y = 0
d = 0
score = 0
count = 0

for _ in range(n):
    array.append(list(map(int, input().split())))

# 동북서남
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def roll(d):
    # 동서남북 순서
    if d == 0:
        temp = dice[1][1]
        dice[1][1] = dice[1][0]
        dice[1][0] = dice[3][1]
        dice[3][1] = dice[1][2]
        dice[1][2] = temp
    elif d == 1:
        temp = dice[1][1]
        dice[1][1] = dice[2][1]
        dice[2][1] = dice[3][1]
        dice[3][1] = dice[0][1]
        dice[0][1] = temp
    elif d == 2:
        temp = dice[1][1]
        dice[1][1] = dice[1][2]
        dice[1][2] = dice[3][1]
        dice[3][1] = dice[1][0]
        dice[1][0] = temp
    elif d == 3:
        temp = dice[1][1]
        dice[1][1] = dice[0][1]
        dice[0][1] = dice[3][1]
        dice[3][1] = dice[2][1]
        dice[2][1] = temp

def get_score(x, y):
    visited = [[False] * m for _ in range(n)]
    queue = deque()
    queue.append([x, y])
    criteria = array[x][y]
    visited[x][y] = True
    cnt = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and array[nx][ny] == criteria:
                queue.append([nx, ny])
                visited[nx][ny] = True
                cnt += 1

    return criteria * cnt


def move():
    global x, y, d, score
    nx = x + dx[d]
    ny = y + dy[d]
    if 0 <= nx < n and 0 <= ny < m:
        x = nx
        y = ny
        roll(d)
    else:
        d = (d + 2) % 4
        x = x + dx[d]
        y = y + dy[d]
        roll(d)
    
    a = dice[3][1]
    b = array[x][y]
    score += get_score(x, y)

    if a < b:
        d = (d + 1) % 4
    elif a > b:
        d = (d + 3) % 4
    
while count < k:
    count += 1
    move()

print(score)
