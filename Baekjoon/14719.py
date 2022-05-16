h, w = map(int, input().split())
array = list(map(int, input().split()))
rain = 0
levels = [[0]*w for _ in range(h) ]

for i in range(h):
    for j in range(w):
        if array[j] > i:
            levels[i][j] = 1

for level in levels:
    idx = [i for i, value in enumerate(level) if value == 1]
    for x in range(1, len(idx)):
        diff = idx[x] - idx[x-1]
        if diff > 1:
            rain += (diff - 1)

print(rain)
