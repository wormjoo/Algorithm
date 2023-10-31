n = int(input())
current = input()
now = list(map(int, current))
now2 = list(map(int, current))
goal = list(map(int, input()))

answer = 1e9
count = 0

for i in range(1, n):    
    if now[i - 1] != goal[i - 1]:
        count += 1
        now[i - 1] = int(not now[i - 1])
        now[i] = int(not now[i])
        if i != n - 1:
            now[i + 1] = int(not now[i + 1])

if now == goal:
    answer = min(answer, count)

now2[0] = int(not now2[0])
now2[1] = int(not now2[1])
count = 1

for i in range(1, n):
    if now2[i - 1] != goal[i - 1]:
        count += 1
        now2[i - 1] = int(not now2[i - 1])
        now2[i] = int(not now2[i])
        if i != n - 1:
            now2[i + 1] = int(not now2[i + 1])

if now2 == goal:
    answer = min(answer, count)


if answer == 1e9:
    print('-1')
else:
    print(answer)
