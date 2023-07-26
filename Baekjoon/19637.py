import sys
input = sys.stdin.readline

n, m = map(int, input().split())
criteria = []

for _ in range(n):
    s, upper = map(str, input().split())
    criteria.append((s, int(upper)))

for _ in range(m):
    power = int(input())
    start, end = 0, n - 1

    while start <= end:
        mid = (start + end) // 2
        if power > criteria[mid][1]:
            start = mid + 1
        else:
            end = mid - 1

    print(criteria[start][0])
        