INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for _ in range(n + 1)]
path = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        path[a][b] = [a, b]
        if a == b:
            graph[a][b] = 0
            path[a][b] = [0]

for _ in range(m):
    a, b, c = map(int, input().split())
    if graph[a][b] > c:
        graph[a][b] = c

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if graph[a][b] > graph[a][k] + graph[k][b]:
                path[a][b] = path[a][k] + path[k][b][1:]
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            print("0", end=" ")
        else:
            print(graph[i][j], end=" ")
    print()

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == 0 or graph[i][j] == INF:
            print(0)
        else:
            print(len(path[i][j]), *path[i][j])
