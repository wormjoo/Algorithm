number = list(map(int, input()))

x = 0
for i in range(1, 30000):
  for j in list(map(int, str(i))):
    if x < len(number) and number[x] == j:
      x += 1
  if x >= len(number):
      print(i)
      break
