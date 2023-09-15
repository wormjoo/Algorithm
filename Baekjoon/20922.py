n, k = map(int, input().split())
a = list(map(int, input().split()))
counter = [0] * (max(a) + 1)
answer = 0
start, end = 0, 0

while start < n:
    if counter[a[start]] < k:
        counter[a[start]] += 1
        start += 1
    else:
        counter[a[end]] -= 1
        end += 1
    answer = max(answer, start - end)

print(answer)
