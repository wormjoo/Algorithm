n = int(input())
dx = [1, 0, -1, 0]
dy = [0, -1, 0 , 1]
direction = [[0]]
cnt = 0

for i in range(10):
    temp = sum(direction, [])
    direction.append(list(reversed(temp)))
    for j in range(len(direction[-1])):
        direction[-1][j] %= 4
        direction[-1][j] += 1

coordinate = []

for _ in range(n):
    x, y, d, g = map(int, input().split())
    coordinate.append((x, y))
    for i in range(g + 1):
        for j in direction[i]:
            m = (j + d) % 4
            x = x + dx[m]
            y = y + dy[m]
            coordinate.append((x, y))
    
coordinate = list(set(coordinate))

for x, y in coordinate:
    if ((x+1, y+1) in coordinate) and ((x+1, y) in coordinate) and ((x, y+1) in coordinate):
        cnt += 1

print(cnt)