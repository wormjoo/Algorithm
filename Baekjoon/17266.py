import math

n = int(input())
m = int(input())
streetlamp = list(map(int, input().split()))

result = max(streetlamp[0], n - streetlamp[-1])

for x in range(1, m):
    result = max(math.ceil((streetlamp[x] - streetlamp[x - 1]) / 2), result)

print(result)
