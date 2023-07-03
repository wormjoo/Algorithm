n, new_score, p = map(int, input().split())
ranking_list = []
rank = -1

if n > 0:
    ranking_list = list(map(int, input().split()))
    for i in range(n, p):
        ranking_list.append(-1)
else:
    rank = 1

i = 0
while i < p and rank < 0:
    if new_score >= ranking_list[i] and new_score > ranking_list[p - 1]:
        rank = i + 1
    i += 1

print(rank)
