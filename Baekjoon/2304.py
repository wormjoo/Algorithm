n = int(input())
roofs = []
head = [0, 0]

for _ in range(n):
  l, h = map(int, input().split())
  roofs.append([l, h])

roofs.sort()
index = 0

for i in range(n):
  if head[1] <= roofs[i][1]:
    head = [roofs[i][0], roofs[i][1]]
    index = i

x, y = roofs[0][0], roofs[0][1]
area = head[1]

for i in range(1, index + 1):
  if roofs[i][1] >= y:
    area += (roofs[i][0] - x) * y
    x, y = roofs[i][0], roofs[i][1]

x, y = roofs[-1][0], roofs[-1][1]

for i in range(n - 1, index - 1, -1):
  if y < roofs[i - 1][1]:
    area += (x - roofs[i - 1][0]) * y
    x, y = roofs[i - 1][0], roofs[i - 1][1]

print(area)
