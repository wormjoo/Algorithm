INF = 1e9

n = int(input())
graph = [[INF] * n for _ in range(n)]
result = [[0] * n for _ in range(n)]

for i in range(n):
    array = list(map(int, input().split()))
    for j in range(n):
        if array[j] == 1:
            graph[i][j] = 1

for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(n):
    for j in range(n):
        if graph[i][j] != INF:
            result[i][j] = 1

for i in range(n):
    print(*result[i])
