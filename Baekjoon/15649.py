from itertools import permutations

n, m = map(int, input().split())
array = [i for i in range(1, n + 1)]
items = list(permutations(array, r=m))

for item in items:
  print(*item)