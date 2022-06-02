from itertools import combinations
n = int(input())
num = [str(x) for x in range(10)]
result = []

for i in range(10):
    result.extend(list(map(''.join, combinations(num, i + 1))))

for i in range(len(result)):
    result[i] = int(''.join(sorted(result[i], reverse=True)))

result.sort()

if n > len(result):
    print(-1)
else:
    print(result[n - 1])