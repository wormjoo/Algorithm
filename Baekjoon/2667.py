from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    count = 0
    
    if space[x][y] > 0:
        count += 1
        space[x][y] = 0
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                if space[nx][ny] == 0:
                    continue
                if space[nx][ny] == 1:
                    space[nx][ny] = 0
                    count += 1
                    queue.append((nx, ny))

    if count > 0:
        town.append(count)

n = int(input())
space = []
town = []

for _ in range(n):
    space.append(list(map(int, input())))

for i in range(n):
    for j in range(n):
        bfs(i, j)

town.sort()
total = len(town)
print(total)
for i in range(total):
    print(town[i])
