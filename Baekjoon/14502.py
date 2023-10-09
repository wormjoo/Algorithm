from copy import deepcopy
from itertools import combinations
from collections import deque

n, m = map(int, input().split())
array = []
virus = []
none = []

for _ in range(n):
    array.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if array[i][j] == 2:
            virus.append([i, j])
        if array[i][j] == 0:
            none.append([i, j])

com = list(combinations(none, 3))

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def bfs(temp):
    queue = deque(virus)
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and temp[nx][ny] == 0:
                temp[nx][ny] = 2
                queue.append([nx, ny])
    
answer = 0

for ([xa, ya], [xb, yb], [xc, yc]) in com:
    if array[xa][ya] == 0 and array[xb][yb] == 0 and array[xc][yc] == 0:
        temp = deepcopy(array)
        count = 0
        temp[xa][ya], temp[xb][yb], temp[xc][yc] = 1, 1, 1
        bfs(temp)

        for i in range(n):
            count += temp[i].count(0)
        
        answer = max(answer, count)

print(answer)
