n = int(input())
triangle = []
d = []

for i in range(1, n + 1):
    triangle.append(list(map(int, input().split())))
    d.append([0] * i)

if n == 1:
    print(triangle[0][0])
else:
    for i in range(n):
        for j in range(i + 1):
            d[i][j] = triangle[i][j]
            if j == 0:
                d[i][j] = d[i - 1][j] + triangle[i][j]
            elif j == i:
                d[i][j] = d[i - 1][j - 1] + triangle[i][j]
            else:
                d[i][j] = max(d[i - 1][j - 1], d[i - 1][j]) + triangle[i][j]

    print(max(d[n - 1]))
