import sys

t = int(input())

for i in range(t):
    n = int(input())
    scores = []
    for j in range(n):
        a, b = sys.stdin.readline().split()
        a, b = int(a), int(b)
        scores.append((a, b))
    scores.sort(key = lambda x : x[0])
    
    cnt = 1
    max = scores[0][1]
    for j in range(1, n):
        if max > scores[j][1]:
            cnt += 1
            max = scores[j][1]
    print(cnt)
