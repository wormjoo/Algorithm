import itertools

n = int(input())
train = list(map(int, input().split()))
limit = int(input())

s = [0]
s.extend(list(itertools.accumulate(train)))

d = [[0] * (n + 1) for _ in range(4)]

for i in range(1, 4):
    for j in range(i * limit, n + 1):
        if i == 1:
            d[i][j] = max(d[i][j - 1], s[j] - s[j - limit])
        else:
            d[i][j] = max(d[i][j - 1], d[i - 1][j - limit] + s[j] - s[j - limit])

print(d[3][n])