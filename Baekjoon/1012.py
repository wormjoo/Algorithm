import sys
sys.setrecursionlimit(10**6) # recursion error 방지

def dfs(x, y):
    if x <= -1 or x>= n or y <= -1 or y >= m:
        return False
    if array[x][y] == 1:
        array[x][y] = 2
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

t = int(input())

for _ in range(t):
  m, n, k = map(int, input().split())
  array = [[0]*m for i in range(n)]
  count = 0

  for i in range(k):
    x, y = map(int, input().split())
    array[y][x] = 1

  for j in range(n):
    for k in range(m):
      if dfs(j, k) == True:
        count += 1
  print(count)
