def section(x, y, d1, d2):
    global n
    first_people, second_people, third_people, fourth_people, fifth_people = 0, 0, 0, 0, 0
    for r in range(n):
        for c in range(n):
            if 1 <= r < x + d1 and 1 <= c <= y:
                first_people += array[r - 1][c - 1]
            elif 1 <= r <= x + d2 and y < c < n:
                second_people += array[r - 1][c - 1]
            elif x + d1 <= r <= n and 1 <= c < y - d1 + d2:
                third_people += array[r - 1][c - 1]
            elif x + d2 < r <= n and y - d1 + d2 <= c <= n:
                fourth_people += array[r - 1][c - 1]
            else:
                fifth_people += array[r - 1][c - 1]

    ward[0].append(first_people)
    ward[1].append(second_people)
    ward[2].append(third_people)
    ward[3].append(fourth_people)
    ward[4].append(fifth_people)

n = int(input())
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

ward = [[] for _ in range(5)]
cnt = 0

for x in range(1, n + 1):
    for y in range(1, n + 1):
        d1_list = [i for i in range(1, n - x)]
        for d1 in d1_list:
            d2_list = [i for i in range(1, n - x - d1)]
            for d2 in d2_list:
                if d1 >= 1 and d2 >= 1 and 1 <= x < x+d1+d2 <= n and 1 <= y-d1 < y < y+d2 <= n:
                    section(x, y, d1, d2)
                    cnt += 1

result = 10000
max_people = 0
min_people = 10000

for i in range(cnt):
    max_people = 0
    min_people = 0
    for j in range(5):
        max_people = max(ward[j][i], max_people)
        min_people = min(ward[j][i], min_people)
        result = min(max_people - min_people, result)

print(result)