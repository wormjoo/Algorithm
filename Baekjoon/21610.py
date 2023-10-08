n, m = map(int, input().split())
array = []

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

diagonal = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

for _ in range(n):
    array.append(list(map(int, input().split())))

cloud = [[n - 1, 0], [n - 1, 1], [n - 2, 0], [n - 2, 1]]

for i in range(m):
    d, s = map(int, input().split())
    visited = [[False] * n for _ in range(n)]
    cloud = [[c[0] + (dx[d - 1] * s), c[1] + (dy[d - 1] * s)] for c in cloud ]

    for j in range(len(cloud)):
        if cloud[j][0] < 0:
            cloud[j][0] = n - (abs(cloud[j][0]) % n)
        if cloud[j][0] >= n:
            cloud[j][0] %= n

        if cloud[j][1] < 0:
            cloud[j][1] = n - (abs(cloud[j][1]) % n)
        if cloud[j][1] >= n:
            cloud[j][1] %= n

    for r, c in cloud:
        array[r][c] += 1
        visited[r][c] = True
    
    for r, c in cloud:
        count = 0
        for x, y in diagonal:
            if 0 <= r + x < n and 0 <= c + y < n and array[r + x][c + y] > 0:
                count += 1
        array[r][c] += count

    cloud = []
    for r in range(n):
        for c in range(n):
            if array[r][c] >= 2 and not visited[r][c]:
                array[r][c] -= 2
                cloud.append([r, c])

answer = 0

for i in range(n):
    answer += sum(array[i])

print(answer)
