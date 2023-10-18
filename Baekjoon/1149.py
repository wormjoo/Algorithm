INF = 10000001
n = int(input())
cost = [[INF, INF, INF] for _ in range(n)]

for i in range(n):
    r, g, b = map(int, input().split())
    if i == 0:
        cost[i] = [r, g, b]
    else:
        for j in range(3):
            if j == 0:
                cost[i][j] = min(cost[i - 1][1], cost[i - 1][2]) + r
            elif j == 1:
                cost[i][j] = min(cost[i - 1][0], cost[i - 1][2]) + g
            elif j == 2:
                cost[i][j] = min(cost[i - 1][0], cost[i - 1][1]) + b

print(min(cost[n - 1]))
