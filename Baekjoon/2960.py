n, k = map(int, input().split())
cnt = 0
num = [True] * (n + 1)
for i in range(2, len(num) + 1):
    for j in range(i, n + 1, i):
        if num[j] == True:
            num[j] = False
            cnt += 1
            if cnt == k:
                print(j)
                break