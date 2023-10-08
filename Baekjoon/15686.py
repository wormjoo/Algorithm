from itertools import combinations

n, m = map(int, input().split())
array = []
chickens = []
houses = []

for _ in range(n):
    array.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if array[i][j] == 1:
            houses.append([i, j])
        elif array[i][j] == 2:
            chickens.append([i, j])

com = list(combinations(chickens, m))

answer = 5000
for not_closure in com:
    distance = 0
    for x, y in houses:
        d = []
        for r, c in not_closure:
            d.append(abs(x - r) + abs(y - c))
        distance += min(d)
    answer = min(answer, distance)

print(answer)
