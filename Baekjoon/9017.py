from collections import Counter
from collections import defaultdict

t = int(input())

for _ in range(t):
    n = int(input())
    team_number = list(map(int, input().split()))
    counter = Counter(team_number)
    score = 1

    result = defaultdict(list)
    for i in range(n):
        if counter[team_number[i]] == 6:
            result[team_number[i]].append(score)
            score += 1

    sum_score = {}
    for key, value in result.items():
        sum_score[key] = [sum(value[:4]), sum(value[:5])]

    rank = sorted(sum_score.items(), key=lambda x: x[1])
    print(rank[0][0])
