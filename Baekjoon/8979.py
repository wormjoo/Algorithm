n, k = map(int, input().split())
medal_info = []

for _ in range(n):
    medal_info.append(list(map(int, input().split())))

medal_info.sort(key=lambda x: (-x[1], -x[2], -x[3]))
medal_info[0].append(1)

if medal_info[0][0] == k:
    print(medal_info[0][4])
else:
    for i in range(1, n):
        if (
            medal_info[i - 1][1] == medal_info[i][1]
            and medal_info[i - 1][2] == medal_info[i][2]
            and medal_info[i - 1][3] == medal_info[i][3]
        ):
            medal_info[i].append(medal_info[i - 1][4])
        else:
            medal_info[i].append(i + 1)

        if medal_info[i][0] == k:
            print(medal_info[i][4])
