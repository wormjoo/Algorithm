def quad_tree(x, y, n):
  global result
  array = video[x][y]
  for i in range(x, x + n):
    for j in range(y, y + n):
      if array != video[i][j]:
        result += "("
        quad_tree(x, y, n // 2)
        quad_tree(x, y + n // 2, n // 2)
        quad_tree(x + n // 2, y, n // 2)
        quad_tree(x + n // 2, y + n // 2, n // 2)
        result += ")"
        return
  result += str(array)

n = int(input())
video = []
result = ''

for i in range(n):
  video.append(list(map(int, input())))

quad_tree(0, 0, n)
print(result)