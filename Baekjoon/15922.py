n = int(input())
current = []
length = 0

for i in range(n):
  x, y = map(int, input().split())
  if i == 0:
    current.append([x, y])
  else:
    if y < current[i - 1][1]:
      current.append(current[i - 1])
      current[i - 1] = [0, 0]
    elif x < current[i - 1][1]:
      current[i - 1][1] = x
      current.append([x, y])
    else:
      current.append([x, y])

for c in current:
  length += abs(c[1] - c[0])

print(length)