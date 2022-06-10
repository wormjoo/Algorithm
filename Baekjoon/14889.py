from itertools import combinations, permutations
n = int(input())
array = []
com = list(combinations([x for x in range(2, n + 1)], n//2 - 1))
start = []
link = []
result = 100

for i in range(len(com)):
    start.append(list(com[i]))
    start[i].insert(0, 1)
    temp = []
    for j in range(1, n + 1):
        if j not in start[i]:
            temp.append(j)
    link.append(temp)

for i in range(n):
    array.append(list(map(int, input().split())))

for x in range(len(start)):
    start_score = 0
    link_score = 0
    s_per = list(permutations(start[x], 2))
    for p in s_per:
        start_score += array[p[0] - 1][p[1] - 1]
    l_per = list(permutations(link[x], 2))
    for p in l_per:
        link_score += array[p[0] - 1][p[1] - 1]
    result = min(abs(start_score-link_score), result)

print(result)