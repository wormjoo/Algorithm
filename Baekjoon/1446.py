n, d = map(int, input().split())
roads = []
dp = [i for i in range(d + 1)]

for i in range(n):
    roads.append(list(map(int, input().split())))

roads.sort(key=lambda x:(x[0], x[1], x[2]))

for road in roads:
    s, e, w = road
    print(s, e, w)
    if e <= d:
        dp[e] = min(dp[s] + w, dp[e])
    for j in range(s, d + 1):
        dp[j] = min(dp[j - 1] + 1, dp[j])

print(dp[d])