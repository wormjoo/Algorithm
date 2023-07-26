T = int(input())

for _ in range(T):
    n, k, t, m = map(int, input().split())
    information = [[0] * (k + 1) for _ in range(n + 1)]
    order = [[] for x in range(n + 1)]

    for x in range(m):
        i, j, s = map(int, input().split())
        order[i].append((x + 1))
        information[i][j] = max(information[i][j], s)

    ranking = []
    for i in range(1, n + 1):
        ranking.append([i, sum(information[i]), len(order[i]), max(order[i])])
    
    ranking.sort(key=lambda x:(-x[1], x[2], x[3]))

    for i in range(n):
        if ranking[i][0] == t:
            print(i + 1)
    