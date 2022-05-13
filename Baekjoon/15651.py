from itertools import product

n, m = map(int, input().split())
array = [i for i in range(1, n + 1)]
items = list(product(array, repeat=m))

for item in items:
  print(*item)