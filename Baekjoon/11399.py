n = int(input())
s = list(map(int, input().split()))

result = 0
s = sorted(s)
for i in range(n):
    for j in range(i + 1):
        result += s[j]
print(result)
