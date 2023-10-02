n, m = map(int, input().split())
array = []
min_value = 100 * n
dp = [[[0,0,0] for _ in range(m)]] + [[[min_value, min_value, min_value] for _ in range(m)] for _ in range(n)]

for _ in range(n):
    array.append(list(map(int, input().split())))

for i in range(1, n + 1):
    for j in range(m):
        if j < m - 1:
            dp[i][j][0] = min(dp[i - 1][j + 1][1], dp[i - 1][j + 1][2]) + array[i - 1][j]
        
        dp[i][j][1] = min(dp[i - 1][j][0], dp[i - 1][j][2]) + array[i - 1][j]

        if 0 < j:
            dp[i][j][2] = min(dp[i - 1][j - 1][1], dp[i - 1][j - 1][0]) + array[i - 1][j]

for d in dp[n]:
    for value in d:
        min_value = min(min_value, value)

print(min_value)
