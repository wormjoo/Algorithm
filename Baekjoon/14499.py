def roll(command):
  a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
  if command == 1: #동
      dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c
  elif command == 2: #서
      dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d
  elif command == 3: #북
      dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b
  else:
      dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e

n, m, x, y, k = map(int, input().split())
array = []
dice = [0, 0, 0, 0, 0, 0]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
current = 0

for i in range(n):
  array.append(list(map(int, input().split())))

command = list(map(int, input().split()))
nx, ny = x, y

for c in command:
  nx += dx[c - 1]
  ny += dy[c - 1]

  if nx < 0 or nx >= n or ny < 0 or ny >= m:
    nx -= dx[c - 1]
    ny -= dy[c - 1]
    continue

  roll(c)

  if array[nx][ny] == 0:
    array[nx][ny] = dice[-1]
  else:
    dice[-1] = array[nx][ny]
    array[nx][ny] = 0
  
  print(dice[0])
