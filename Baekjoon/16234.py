from collections import deque

INF = 1000000
n, l, r = map(int, input().split())
country = []
visited = [[False] * n for _ in range(n)]
team = [[-1] * n for _ in range(n)]

for _ in range(n):
    country.append(list(map(int, input().split())))

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

population = [0] * (n ** 2 + 1)
union = [1] * (n ** 2 + 1)

def bfs(x, y, num):
    global population, union
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True
    population[num] = country[x][y]
    team[x][y] = num

    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and l <= abs(country[x][y] - country[nx][ny]) <= r:
                population[num] += country[nx][ny]
                visited[nx][ny] = True
                union[num] += 1
                team[nx][ny] = num
                queue.append([nx, ny])

def move():
    flag = False
    num = 0

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                num += 1
                bfs(i, j, num)
    
    for i in range(n):
        for j in range(n):
            if union[team[i][j]] > 1:
                country[i][j] = population[team[i][j]] // union[team[i][j]]
                flag = True
    
    return flag

day = 0

while 1:
    population = [0] * (n ** 2 + 1)
    union = [1] * (n ** 2 + 1)
    visited = [[False] * n for _ in range(n)]
    flag = move()
    if not flag:
        break
    day += 1

print(day)
