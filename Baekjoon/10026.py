from collections import deque

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def bfs(x, y, color):
    global visited, count
    queue = deque()
    
    if not visited[x][y] and array[x][y] == color:
        count += 1
        queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and array[nx][ny] == color:
                visited[nx][ny] = True
                queue.append((nx, ny))

n = int(input())
array = []
not_color_blindness = 0
color_blindness = 0
count = 0

for _ in range(n):
    array.append(list(input()))

visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        bfs(i, j, 'R')
        bfs(i, j, 'G')
        bfs(i, j, 'B')

not_color_blindness = count
visited = [[False] * n for _ in range(n)]
count = 0

for i in range(n):
    for j in range(n):
        if array[i][j] == 'G':
            array[i][j] = 'R'

for i in range(n):
    for j in range(n):
        bfs(i, j, 'R')
        bfs(i, j, 'B')

color_blindness = count

print(not_color_blindness, color_blindness)
