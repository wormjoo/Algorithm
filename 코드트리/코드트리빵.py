from collections import deque

n, m = map(int, input().split())
graph = []
basecamps = []
basecamp_count = 0
store = [(-1, -1)]
people = [[-1, -1] for _ in range(m + 1)]
blocked = [[False] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]
step = [[0] * n for _ in range(n)]
left = m

for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            basecamps.append([i, j])
            basecamp_count += 1

for i in range(m):
    x, y = map(int, input().split())
    store.append([x - 1, y - 1])
    graph[x - 1][y - 1] = -(i + 1)

# ↑, ←, →, ↓
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

t = 0

def bfs(x, y):
    for i in range(n):
        for j in range(n):
            visited[i][j] = False
            step[i][j] = 0
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True
    step[x][y] = 0
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not blocked[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = True
                step[nx][ny] = step[x][y] + 1
                queue.append([nx, ny])

def moveAll():
    for i in range(1, m + 1):
        if people[i] == [-1, -1]:
            continue

        bfs(store[i][0], store[i][1])
        
        distance = 300
        min_x, min_y = -1, -1
        for d in range(4):
            nx = people[i][0] + dx[d]
            ny = people[i][1] + dy[d]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] and not blocked[nx][ny] and distance > step[nx][ny]:
                distance = step[nx][ny]
                min_x, min_y = nx, ny

        people[i] = [min_x, min_y]

def arrived():
    global left
    for i in range(1, m + 1):
        if store[i] == people[i] and people[i] != [-1, -1]:
            blocked[store[i][0]][store[i][1]] = True
            store[i] = [-1, -1]
            people[i] = [-1, -1]
            left -= 1

def go_to_basecamp():
    global t
    if t <= m:
        bfs(store[t][0], store[t][1])
        distance = 300
        basecamp = [-1, -1]
        for i in range(basecamp_count):
            if visited[basecamps[i][0]][basecamps[i][1]] and not blocked[basecamps[i][0]][basecamps[i][1]] and basecamps[i] != [-1, -1] and step[basecamps[i][0]][basecamps[i][1]] < distance:
                distance = step[basecamps[i][0]][basecamps[i][1]]
                basecamp = basecamps[i]
                
        blocked[basecamp[0]][basecamp[1]] = True
        people[t] = basecamp

while 1:
    if left == 0:
        break
    t += 1
    
    moveAll()
    arrived()
    go_to_basecamp()

print(t)
