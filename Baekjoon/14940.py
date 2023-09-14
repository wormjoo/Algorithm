from collections import deque

n, m = map(int, input().split())
graph = []
a, b = -1, -1

for i in range(n):
    array = list(map(int, input().split()))
    graph.append(array)

    for j in range(m):
        if array[j] == 2:
            a = i
            b = j

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visit = [[False] * m for _ in range(n)]
graph[a][b] = 0
visit[a][b] = True

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny] and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
                visit[nx][ny] = True
    return graph

graph = bfs(a, b)

for i in range(n):
    for j in range(m):
        if abs(a - i) + abs(b - j) != 1 and graph[i][j] == 1:
            graph[i][j] = -1

for i in range(n):
    print(*graph[i])
