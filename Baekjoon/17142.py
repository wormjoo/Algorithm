from itertools import combinations
from collections import deque

def bfs():
    # 상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and array[nx][ny] != 1:
                visited[nx][ny] = 1
                queue.append((nx, ny))
                board[nx][ny] = board[x][y] + 1

n, m = map(int, input().split())
array = []
virus = []
result = 1000000
nothing = 0

for i in range(n):
    array.append(list(map(int, input().split())))
    for j in range(n):
        if array[i][j] == 2:
            virus.append((i, j))
        if array[i][j] != 1:
            nothing += 1

coms = list(combinations(virus, r=m))

for com in coms:
    visited = [[False] * n for _ in range(n)]
    board = [[-1] * n for _ in range(n)]
    queue = deque()

    for x, y in com:
        visited[x][y] = True
        board[x][y] = 0
        queue.append((x, y))
    bfs()
    cnt = 0
    for i in visited:
        cnt += i.count(1)
    if nothing == cnt:
        max_board = 0
        for i in range(n):
            for j in range(n):
                if array[i][j] != 1 and (i, j) not in virus:
                    max_board = max(board[i][j], max_board)
        result = min(max_board, result)
        
if result == 1000000:
    print(-1)
else:
    print(result)
