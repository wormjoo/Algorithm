from itertools import combinations

n, s = map(int, input().split())
sequence = list(map(int, input().split()))

count = 0
for i in range(n + 1):
    parts = list(combinations(sequence, i))
    for part in parts:
        if len(part) > 0 and sum(part) == s:
            count += 1

print(count)