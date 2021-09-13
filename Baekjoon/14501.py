N = int(input())
T = list()
P = list()
dp = [0] * (N+1)

for i in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
dp.append(0) # list 초과범위때문에 하나 더 넣음

for i in range(N-1, -1, -1):
    if (N-i) < T[i]:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(P[i] + dp[i+T[i]], dp[i+1])

print(max(dp))
